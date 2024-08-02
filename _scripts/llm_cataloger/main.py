import os
import yaml
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Configuration
INPUT_DIRECTORY = "../../_posts"
OUTPUT_DIRECTORY = "./_ignore_output"
PREDEFINED_CATEGORIES = [
"Game Mastering",
"Player Corner",
"Homebrew Workshop",
"Indie Games",
"Industry Insights",
"Reviews & Recommendations",
"Community Discussions",
"Resources & Tools",
"Announcements",
]

# Initialize the ChatAnthropic model
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
llm = ChatAnthropic(model="claude-3-sonnet-20240229", anthropic_api_key=api_key)

from typing import Optional, Tuple
from pathlib import Path

def parse_jekyll_post(file_path: Path) -> Tuple[Optional[str], Optional[dict]]:
    """
    Parse a Jekyll post file and extract the front matter and post content.

    Args:
        file_path (Path): The path to the Jekyll post file.

    Returns:
        Tuple[Optional[str], Optional[dict]]: A tuple containing the post content and front matter.
            If the file does not have valid front matter, None is returned for both values.
    """
    encodings = ['utf-8', 'iso-8859-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()

            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"Warning: File {file_path} does not appear to have valid front matter. Skipping.")
                return None, None

            _, front_matter, post_content = parts

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

    return None, None

def create_category_assignment_chain() -> LLMChain:
    prompt = PromptTemplate(
        input_variables=["categories", "post_content"],
        template="""You are an expert in categorizing TTRPG and DnD fan content. The following is a list of 
        catagories and a short description of each catagory. Assign one or more of the following categories to the given blog post content:
            CATAGORY - DESCRIPTION
            {categories}

            Blog post content:
            {post_content}

            Return only the list of assigned categories without description, separated by commas. If no categories apply, return 'None'."""
    )

    return LLMChain(llm=llm, prompt=prompt, verbose=True)

def assign_categories(post_content: str, predefined_categories: List[str], chain: LLMChain) -> List[str]:
    # Prepare the input
    categories_str = ", ".join(predefined_categories)
    truncated_content = post_content[:3000]  # Truncate to 3000 characters
    
    # Print debug information
    # print(f"Categories being sent: {categories_str}")
    # print(f"Content preview being sent: {truncated_content[:100]}...")

    try:
        # Run the chain with explicit keyword arguments
        response = chain.run(categories=categories_str, post_content=truncated_content)
        # print(f"Raw response from LLM: {response}")

        if response.strip().lower() == 'none':
            return []

        assigned_categories = [cat.strip() for cat in response.split(',')]
        valid_categories = [cat for cat in assigned_categories if cat in predefined_categories]

        if not valid_categories:
            print(f"Warning: No valid categories assigned. Raw response: {response}")

        return valid_categories

    except Exception as e:
        print(f"Error in assign_categories: {e}")
        return []


def write_jekyll_post(file_path: Path, front_matter: dict, post_content: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("---\n")
            yaml.dump(front_matter, file, default_flow_style=False, allow_unicode=True)
            file.write("---\n\n")
            file.write(post_content)
        print(f"Successfully wrote file: {file_path}")
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def process_post(input_file: Path, output_file: Path, category_chain: LLMChain) -> None:
    post_content, front_matter = parse_jekyll_post(input_file)
    if post_content is None or front_matter is None:
        print(f"Skipping {input_file} due to parsing error.")
        return

    print(f"Processing file: {input_file}")
    # print(f"Post content preview: {post_content[:100]}...")
    
    assigned_categories = assign_categories(post_content, PREDEFINED_CATEGORIES, category_chain)
    if 'catagory' in front_matter.keys():
        del front_matter['catagory']

    print(f"Assigned categories: {assigned_categories}")
    
    if not assigned_categories:
        print(f"Warning: No categories assigned for {input_file}")

    post_date = parse_date(front_matter, input_file.name)
    front_matter['date'] = post_date.strftime('%Y-%m-%d %H:%M')
    
    front_matter['categories'] = assigned_categories
    write_jekyll_post(output_file, front_matter, post_content)
    print(f"Finished processing: {input_file}")

def parse_date(front_matter: Dict[str, Any], filename: str) -> datetime:
    """
    Parses the date from the front matter or filename and returns a datetime object.

    Args:
        front_matter (Dict[str, Any]): A dictionary containing the front matter data.
        filename (str): The name of the file.

    Returns:
        datetime: The parsed date as a datetime object.

    Raises:
        ValueError: If the date format in the front matter is unexpected.

    """
    if 'date' in front_matter:
        date = front_matter['date']
        if isinstance(date, datetime):
            return date
        elif isinstance(date, str):
            return datetime.strptime(date[:10], '%Y-%m-%d %HH:%MM')
        else:
            raise ValueError(f"Unexpected date format in front matter: {date}")
    else:
        date_str = filename[:10]  # Extract YYYY-MM-DD from filename
        return datetime.strptime(date_str, '%Y-%m-%d %HH:%MM')

def main() -> None:
    category_chain = create_category_assignment_chain()

    input_dir = Path(INPUT_DIRECTORY)
    output_dir = Path(OUTPUT_DIRECTORY)
    output_dir.mkdir(parents=True, exist_ok=True)

    post_list = list(input_dir.glob("*.md"))

    for post_file in post_list:
        output_file = output_dir / post_file.name
        try:
            process_post(post_file, output_file, category_chain)
            print(f"Processed: {post_file.name}")
        except Exception as e:
            print(f"Error processing {post_file.name}: {e}")

if __name__ == "__main__":
    main()