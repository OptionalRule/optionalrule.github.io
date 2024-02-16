import argparse
import pathlib
import re
import html

def extract_title_from_front_matter(content):
    """
    Extract the title from Jekyll front matter in the markdown content.

    Parameters:
    - content: A string containing the markdown content.

    Returns:
    - The title as a string, if found. None otherwise.
    """
    title_match = re.search(r'^title: (.*)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1)
    return None

def remove_jekyll_front_matter(content):
    """
    Remove Jekyll front matter from markdown content.

    Parameters:
    - content: A string containing the markdown content.

    Returns:
    - A string with the Jekyll front matter removed.
    """
    return re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

def remove_liquid_tags(content):
    """
    Remove Liquid template tags from markdown content, including multiline tags.

    Parameters:
    - content: A string containing the markdown content.

    Returns:
    - A string with the Liquid template tags removed.
    """
    # Remove single-line and multiline Liquid tags
    content = re.sub(r'\{\{.*?\}\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\{%.*?%\}', '', content, flags=re.DOTALL)
    return content

def clean_html_content(content):
    """
    Strip HTML tags and decode HTML entities in the content.

    Parameters:
    - content: A string containing the HTML content.

    Returns:
    - A string with HTML tags removed and HTML entities decoded.
    """
    # Remove HTML tags
    tag_free_content = re.sub(r'<[^>]+>', '', content)
    
    # Decode HTML entities
    decoded_content = html.unescape(tag_free_content)
    
    return decoded_content


def combine_markdown_files(directory_path, output_file_path):
    """
    Combine the content of all markdown files in the given directory into a single file
    after removing Jekyll front matter and Liquid template tags, and adding the extracted title at the start.

    Parameters:
    - directory_path: Path to the directory containing markdown files.
    - output_file_path: Path to the output file where combined markdown will be written.
    """
    directory = pathlib.Path(directory_path)
    output_file = pathlib.Path(output_file_path)

    if not directory.is_dir():
        print(f"Directory {directory_path} does not exist.")
        return

    try:
        with output_file.open('w', encoding='utf-8') as outfile:
            for file in directory.glob('*.md'):
                with file.open('r', encoding='utf-8') as infile:
                    content = infile.read()
                    title = extract_title_from_front_matter(content)
                    content_without_front_matter = remove_jekyll_front_matter(content)
                    content_without_html_tags = clean_html_content(content_without_front_matter)
                    cleaned_content = remove_liquid_tags(content_without_html_tags)
                    if title:
                        outfile.write(f"# {title}\n\n")
                    outfile.write(cleaned_content + '\n\n')
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"Combined markdown file created at {output_file_path}")

def main():
    """
    Execute the script to combine markdown files into a single file after cleanup.

    This script takes two command line arguments:
    1. directory_path: The path to the directory containing markdown files.
    2. output_file_path: The path for the output file where the combined markdown will be written.

    Example execution:
    python script_name.py ../_posts ./combined_markdown.md

    This will combine all markdown files from '../__posts' into a single markdown file named 'combined_markdown.md',
    with Jekyll front matter and Liquid tags removed, and each post's title added at the start.
    """
    parser = argparse.ArgumentParser(description="Combine markdown files from a directory into a single file after cleaning Jekyll front matter and Liquid tags, adding post titles.")
    parser.add_argument("directory_path", type=str, help="Path to the directory containing markdown files.")
    parser.add_argument("output_file_path", type=str, help="Path for the output combined markdown file.")

    args = parser.parse_args()

    combine_markdown_files(args.directory_path, args.output_file_path)

if __name__ == "__main__":
    main()
