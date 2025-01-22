import argparse
from pathlib import Path
from markitdown import MarkItDown

def convert_paper(arxiv_id: str) -> None:
  papers_dir = Path('papers')
  paper = papers_dir / f'arxiv_{arxiv_id}.pdf'
  md = MarkItDown()
  result = md.convert(f'{paper}')
  
  with open(f'papers/arxiv_{arxiv_id}.md', 'w', encoding='utf-8') as file:
    file.write(result.text_content)

def main():
  parser = argparse.ArgumentParser(description='Convert a paper from arXiv given its ID')
  parser.add_argument('arxiv_id', help='The arXiv ID of the paper (e.g., 2101.12345)')
  args = parser.parse_args()
  convert_paper(args.arxiv_id)

if __name__ == '__main__':
    main()

