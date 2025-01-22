import argparse
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path
import os


def ai_magick(text: str):
  model = genai.GenerativeModel("gemini-1.5-flash") 
  
  # Generate text using the model
  prompt = f"""
  Please process the following Markdown document which represents an academic paper:

  {text}

  **Tasks:**
  1. **Extract the title** Please try to find the title of the paper.
  2. **Extract the abstract** Please try to find the abstract of the paper.
  3. **Extract the authors** Please try to find the authors of the paper.
  4. **Extract the author contribution statement** Please try to find the statement that says who did what

  **Output format:** 
  * Present the title, abstract and authors in a clear and organized manner.
  * Use Markdown formatting for better readability (e.g., headings, bullet points). 
  """

  response = model.generate_content(prompt) 
  print(response.text) 

def parse_paper(arxiv_id: str) -> None:
  papers_dir = Path('papers')
  paper = papers_dir / f'arxiv_{arxiv_id}.md'
  with open(paper, 'r') as file:
    content = file.read()
    ai_magick(content)

def main():
  load_dotenv()

  parser = argparse.ArgumentParser(description='Convert a paper from arXiv given its ID')
  parser.add_argument('arxiv_id', help='The arXiv ID of the paper (e.g., 2101.12345)')
  args = parser.parse_args()

  genai.configure(api_key=os.environ["GEMINI_API_KEY"]) 
  parse_paper(args.arxiv_id)

if __name__ == '__main__':
    main()


