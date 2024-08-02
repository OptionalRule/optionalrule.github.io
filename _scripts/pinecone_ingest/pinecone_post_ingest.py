import os
import re
from typing import List, Dict, Any
from datetime import datetime
from urllib.parse import urljoin
import yaml
from pinecone import Pinecone
from transformers import CLIPTokenizer, CLIPTextModel
import torch
from dotenv import load_dotenv


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
BASE_URL = 'https://optionalrule.com/'

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Connect to the existing index
index = pc.Index(PINECONE_INDEX_NAME)

# Initialize the CLIP model and tokenizer
model_name = 'openai/clip-vit-base-patch32'
tokenizer = CLIPTokenizer.from_pretrained(model_name)
model = CLIPTextModel.from_pretrained(model_name)

from typing import Dict, Any
from datetime import datetime

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
            return datetime.strptime(date[:10], '%Y-%m-%d')
        else:
            raise ValueError(f"Unexpected date format in front matter: {date}")
    else:
        date_str = filename[:10]  # Extract YYYY-MM-DD from filename
        return datetime.strptime(date_str, '%Y-%m-%d')
    
def generate_url(date: datetime, filename: str) -> str:
    slug = filename[11:].replace('.md', '')  # Remove date and .md extension
    content_url = f"/{date.year:04d}/{date.month:02d}/{date.day:02d}/{slug}/"
    return urljoin(BASE_URL, content_url)

def extract_posts(posts_dir: str) -> List[Dict[str, Any]]:
    parsed_posts = []
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            with open(os.path.join(posts_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = yaml.safe_load(parts[1])
                    post_content = parts[2].strip()
                    post_content = strip_liquid_tags(post_content)
                    date = parse_date(front_matter, filename)
                    parsed_posts.append({
                        'id': filename,
                        'title': front_matter.get('title', ''),
                        'content': post_content,
                        'url': generate_url(date, filename),
                        'date': date.isoformat()
                    })
    return parsed_posts

def strip_liquid_tags(content: str) -> str:
    # Remove comment tags and their content
    content = re.sub(r'{%\s*comment\s*%}.*?{%\s*endcomment\s*%}', '', content, flags=re.DOTALL)
    
    # Remove raw tags but keep their content
    content = re.sub(r'{%\s*raw\s*%}(.*?){%\s*endraw\s*%}', r'\1', content, flags=re.DOTALL)
    
    # Remove all other liquid tags
    content = re.sub(r'{%.*?%}', '', content)
    
    # Remove liquid output tags
    content = re.sub(r'{{.*?}}', '', content)
    
    # Remove extra whitespace
    content = re.sub(r'\s+', ' ', content).strip()
    
    return content

def preprocess_text(text: str) -> str:
    return text.lower()

def generate_embedding(text: str) -> List[float]:
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=77)
    with torch.no_grad():
        outputs = model(**inputs)
    # The last hidden state will be a 1024-dimensional vector
    return outputs.last_hidden_state[0, 0, :].tolist()

def generate_embeddings(posts: List[Dict[str, Any]]):
    for post in posts:
        text = f"{post['title']} {post['content']}"
        preprocessed_text = preprocess_text(text)
        embedding = generate_embedding(preprocessed_text)
        yield post['id'], embedding, {'title': post['title'], 'url': post['url'], 'date': post['date']}

def index_posts(parsed_posts: List[Dict[str, Any]]):
    batch_size = 100
    vectors = list(generate_embeddings(parsed_posts))
    
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i+batch_size]
        index.upsert(vectors=batch)

def main():
    posts_dir = '../../_posts'  # Adjust this to your Jekyll posts directory
    posts = extract_posts(posts_dir)
    # print(posts)
    index_posts(posts)
    print(f"Indexed {len(posts)} posts in Pinecone.")

if __name__ == '__main__':
    main()