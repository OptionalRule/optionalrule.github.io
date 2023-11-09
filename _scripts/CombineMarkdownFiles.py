import os

def combine_markdown_files(directory_path, output_file_path):
    markdown_contents = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.md'):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                markdown_contents.append(file.read() + '\n\n')
    combined_markdown = ''.join(markdown_contents)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(combined_markdown)
    print(f"Combined markdown file created at {output_file_path}")

if __name__ == "__main__":
    # Replace with the actual path to your markdown files
    directory_path = '../_posts'

    # Replace with the desired output markdown file path
    output_file_path = './combined_markdown.md'

    combine_markdown_files(directory_path, output_file_path)
