"""
Utility script to combine Jekyll blog posts into a single markdown file.
"""
import os
import re
import argparse
from datetime import datetime
import yaml

def read_jekyll_post(file_path):
    """
    Read a Jekyll post file and extract the front matter and content.

    Args:
        file_path (str): The path to the Jekyll post file.

    Returns:
        tuple: A tuple containing the metadata (front matter) as a dictionary and the content as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the file into front matter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, parts[-1].strip()
    
    # Parse the front matter
    try:
        metadata = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        metadata = {}
    
    return metadata, parts[2].strip()

def clean_markdown(content):
    """
    Cleans the given markdown content by removing HTML comments, liquid tags, extra whitespace, and newlines.

    Args:
        content (str): The markdown content to be cleaned.

    Returns:
        str: The cleaned markdown content.
    """
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove liquid tags
    content = re.sub(r'{%.*?%}', '', content, flags=re.DOTALL)
    
    # Remove extra whitespace and newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

def get_post_date(metadata, file_path):
    """
    Get the post date from the metadata or file creation time.

    Args:
        metadata (dict): The metadata dictionary containing the post information.
        file_path (str): The path of the file.

    Returns:
        datetime: The post date as a datetime object.
    """
    if 'date' in metadata:
        try:
            return datetime.strptime(str(metadata['date']), "%Y-%m-%d %H:%M:%S %z")
        except ValueError:
            try:
                return datetime.strptime(str(metadata['date']), "%Y-%m-%d")
            except ValueError:
                pass
    
    # If no valid date in metadata, use file creation time
    return datetime.fromtimestamp(os.path.getctime(file_path))

def process_posts(directory, output_file):
    """
    Process the markdown files in the specified directory and combine them into a single output file.

    Args:
        directory (str): The directory path where the markdown files are located.
        output_file (str): The path of the output file where the combined content will be written.

    Returns:
        None
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.md') or filename.endswith('.markdown'):
                file_path = os.path.join(directory, filename)
                metadata, content = read_jekyll_post(file_path)
                
                # Write post title
                title = metadata.get('title', 'Untitled')
                outfile.write(f"# {title}\n\n")
                
                # Write post date
                date = get_post_date(metadata, file_path)
                outfile.write(f"*Posted on: {date.strftime('%B %d, %Y')}*\n\n")
                
                # Write cleaned content
                cleaned_content = clean_markdown(content)
                outfile.write(cleaned_content)
                
                # Add separator
                outfile.write("\n\n---\n\n")

def main():
    """
    Combine Jekyll blog posts into a single markdown file.

    Args:
        posts_directory (str): Directory containing Jekyll blog posts.
        output_file (str): Path to the output markdown file.
    """
    parser = argparse.ArgumentParser(description="Combine Jekyll blog posts into a single markdown file.")
    parser.add_argument("posts_directory", help="Directory containing Jekyll blog posts")
    parser.add_argument("output_file", help="Path to the output markdown file")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.posts_directory):
        print(f"Error: {args.posts_directory} is not a valid directory.")
        return
    
    process_posts(args.posts_directory, args.output_file)
    print(f"All posts have been combined into {args.output_file}")

if __name__ == "__main__":
    # python combine_markdown_files.py ..\_posts combined_markdown.md
    main()