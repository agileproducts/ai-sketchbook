import argparse
from pathlib import Path
from markitdown import MarkItDown

def convert_paper(filename: str) -> None:
  papers_dir = Path('papers')
  paper = papers_dir / f'{filename}'
  md = MarkItDown()
  result = md.convert(f'{paper}')
  
  with open(f'papers/{filename}.md', 'w', encoding='utf-8') as file:
    file.write(result.text_content)

def main():
  parser = argparse.ArgumentParser(description='Convert a paper from document')
  parser.add_argument('filename', help='filename')
  args = parser.parse_args()
  convert_paper(args.filename)

if __name__ == '__main__':
    main()