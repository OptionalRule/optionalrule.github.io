import os
import yaml
import logging
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Configuration
INPUT_DIRECTORY = Path("../../_posts")
OUTPUT_DIRECTORY = Path("./_ignore_output")
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

def parse_jekyll_post(file_path: Path) -> Tuple[Optional[str], Optional[dict]]:
    """Parse a Jekyll post file and extract the front matter and post content."""
    encodings = ['utf-8', 'iso-8859-1', 'cp1252']

    for encoding in encodings:
        try:
            with file_path.open('r', encoding=encoding) as file:
                content = file.read()

            parts = content.split('---', 2)
            if len(parts) < 3:
                logging.warning(f"File {file_path} does not appear to have valid front matter. Skipping.")
                return None, None

            _, front_matter, post_content = parts

            try:
                front_matter = yaml.safe_load(front_matter.strip())
            except yaml.YAMLError as e:
                logging.warning(f"Error parsing YAML front matter in {file_path}: {e}. Skipping.")
                return None, None

            return post_content.strip(), front_matter

        except UnicodeDecodeError:
            if encoding == encodings[-1]:
                logging.error(f"Unable to decode {file_path} with any of the attempted encodings. Skipping this file.")
                return None, None

    return None, None

def create_category_assignment_chain() -> LLMChain:
    """Create and return a LangChain for category assignment."""
    prompt = PromptTemplate(
        input_variables=["categories", "post_content"],
        template="""You are an expert in categorizing TTRPG and DnD fan content. The following is a list of 
        categories and a short description of each category. Assign one or more of the following categories to the given blog post content:
            CATEGORY - DESCRIPTION
            {categories}

            Blog post content:
            {post_content}

            Return only the list of assigned categories without description, separated by commas. If no categories apply, return 'None'."""
    )

    return LLMChain(llm=llm, prompt=prompt, verbose=True)

def assign_categories(post_content: str, predefined_categories: List[str], chain: LLMChain) -> List[str]:
    """Assign categories to a post using the provided LangChain."""
    categories_str = ", ".join(predefined_categories)
    truncated_content = post_content[:3000]  # Truncate to 3000 characters

    try:
        response = chain.run(categories=categories_str, post_content=truncated_content)

        if response.strip().lower() == 'none':
            return []

        assigned_categories = [cat.strip() for cat in response.split(',')]
        valid_categories = [cat for cat in assigned_categories if cat in predefined_categories]

        if not valid_categories:
            logging.warning(f"No valid categories assigned. Raw response: {response}")

        return valid_categories

    except Exception as e:
        logging.error(f"Error in assign_categories: {e}")
        return []

def write_jekyll_post(file_path: Path, front_matter: dict, post_content: str) -> None:
    """Write the updated Jekyll post to a file."""
    try:
        with file_path.open('w', encoding='utf-8') as file:
            file.write("---\n")
            yaml.dump(front_matter, file, default_flow_style=False, allow_unicode=True)
            file.write("---\n\n")
            file.write(post_content)
        logging.info(f"Successfully wrote file: {file_path}")
    except IOError as e:
        logging.error(f"Error writing to file {file_path}: {e}")

def parse_date(front_matter: Dict[str, Any], filename: str) -> datetime:
    """Parse the date from the front matter or filename."""
    if 'date' in front_matter:
        date = front_matter['date']
        if isinstance(date, datetime):
            return date
        elif isinstance(date, str):
            try:
                return datetime.strptime(date, '%Y-%m-%d %H:%M')
            except ValueError:
                # If the above fails, try parsing without time
                return datetime.strptime(date[:10], '%Y-%m-%d')
        else:
            raise ValueError(f"Unexpected date format in front matter: {date}")
    else:
        date_str = filename[:10]  # Extract YYYY-MM-DD from filename
        return datetime.strptime(date_str, '%Y-%m-%d')

def process_post(input_file: Path, output_file: Path, category_chain: LLMChain) -> None:
    """Process a single Jekyll post file."""
    post_content, front_matter = parse_jekyll_post(input_file)
    if post_content is None or front_matter is None:
        logging.warning(f"Skipping {input_file} due to parsing error.")
        return

    logging.info(f"Processing file: {input_file}")
    
    assigned_categories = assign_categories(post_content, PREDEFINED_CATEGORIES, category_chain)
    front_matter.pop('category', None)  # Remove 'category' if it exists

    logging.info(f"Assigned categories: {assigned_categories}")
    
    if not assigned_categories:
        logging.warning(f"No categories assigned for {input_file}")

    post_date = parse_date(front_matter, input_file.name)
    front_matter['date'] = post_date.strftime('%Y-%m-%d %H:%M')
    
    front_matter['categories'] = assigned_categories
    write_jekyll_post(output_file, front_matter, post_content)
    logging.info(f"Finished processing: {input_file}")

def main() -> None:
    """Main function to process all Jekyll posts."""
    category_chain = create_category_assignment_chain()

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

    post_files = list(INPUT_DIRECTORY.glob("*.md"))
    total_posts = len(post_files)

    for i, post_file in enumerate(post_files, 1):
        output_file = OUTPUT_DIRECTORY / post_file.name
        try:
            process_post(post_file, output_file, category_chain)
            logging.info(f"Processed: {post_file.name} ({i}/{total_posts})")
        except Exception as e:
            logging.error(f"Error processing {post_file.name}: {e}")

    logging.info(f"Finished processing all {total_posts} posts.")

if __name__ == "__main__":
    main()