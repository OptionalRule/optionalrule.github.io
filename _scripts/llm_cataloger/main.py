import os
import yaml
import requests
from pathlib import Path

# Configuration
INPUT_DIRECTORY = "../../_posts"
OUTPUT_DIRECTORY = "./output"
PREDEFINED_CATEGORIES = [
    "Game Mechanics",
    "Worldbuilding",
    "DM Advice",
    "Homebrew Content",
    "Adventure Design",
    "Player Advice",
    "Community Discussion",
    "Product Reviews",
    "Resources",
    "Giveaways",
    "Meta"
]
OLLAMA_API_URL = "http://localhost:11434/api/generate"


def check_ollama_availability():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.status_code == 200
    except requests.RequestException:
        return False


def parse_jekyll_post(file_path):
    encodings = ['utf-8', 'iso-8859-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()

            # Split the content into front matter and post content
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"Warning: File {file_path} does not appear to have valid front matter. Skipping.")
                return None, None

            _, front_matter, post_content = parts

            # Parse the front matter
            try:
                front_matter = yaml.safe_load(front_matter.strip())
            except yaml.YAMLError as e:
                print(f"Warning: Error parsing YAML front matter in {file_path}: {e}. Skipping.")
                return None, None

            return post_content.strip(), front_matter

        except UnicodeDecodeError:
            if encoding == encodings[-1]:
                print(f"Error: Unable to decode {file_path} with any of the attempted encodings. Skipping this file.")
                return None, None

    return None, None  # This line should never be reached, but it's here for completeness


def assign_categories(post_content, predefined_categories):
    prompt = f"""
    Assign one or more of the following categories to the given blog post content:
    {', '.join(predefined_categories)}

    Blog post content:
    {post_content[:1000]}  # Limiting to first 1000 characters for efficiency

    Return only the list of assigned categories, separated by commas.
    """

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        assigned_categories = result['response'].strip().split(', ')
        return [cat for cat in assigned_categories if cat in predefined_categories]
    except requests.RequestException as e:
        print(f"Error communicating with Ollama API: {e}")
        return []


def write_jekyll_post(file_path, front_matter, post_content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("---\n")
            yaml.dump(front_matter, file, default_flow_style=False, allow_unicode=True)
            file.write("---\n\n")
            file.write(post_content)
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")


def process_post(input_file, output_file):
    post_content, front_matter = parse_jekyll_post(input_file)
    if post_content is None or front_matter is None:
        return

    assigned_categories = assign_categories(post_content, PREDEFINED_CATEGORIES)
    front_matter['categories'] = assigned_categories
    write_jekyll_post(output_file, front_matter, post_content)


def main():
    if not check_ollama_availability():
        print("Error: Ollama is not available. Please make sure it's running on http://localhost:11434")
        return

    input_dir = Path(INPUT_DIRECTORY)
    output_dir = Path(OUTPUT_DIRECTORY)
    output_dir.mkdir(parents=True, exist_ok=True)

    for post_file in input_dir.glob("*.md"):
        output_file = output_dir / post_file.name
        try:
            process_post(post_file, output_file)
            print(f"Processed: {post_file.name}")
        except Exception as e:
            print(f"Error processing {post_file.name}: {e}")


if __name__ == "__main__":
    main()