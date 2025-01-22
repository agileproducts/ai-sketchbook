import requests
import argparse
from pathlib import Path

def download_arxiv_paper(arxiv_id: str) -> None:
    """
    Download a paper from arXiv given its ID and save it to a 'papers' directory.
    
    Args:
        arxiv_id (str): The arXiv ID of the paper (e.g., '2101.12345')
    """
    # Create papers directory if it doesn't exist
    papers_dir = Path('papers')
    papers_dir.mkdir(exist_ok=True)
    
    # Construct the PDF URL
    pdf_url = f'https://arxiv.org/pdf/{arxiv_id}.pdf'
    
    try:
        # Send GET request to download the PDF
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Generate output filename
        output_path = papers_dir / f'arxiv_{arxiv_id}.pdf'
        
        # Write the PDF to file
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f'Successfully downloaded paper to {output_path}')
        
    except requests.exceptions.RequestException as e:
        print(f'Error downloading paper: {e}')

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download a paper from arXiv given its ID')
    parser.add_argument('arxiv_id', help='The arXiv ID of the paper (e.g., 2101.12345)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Download the paper
    download_arxiv_paper(args.arxiv_id)

if __name__ == '__main__':
    main()