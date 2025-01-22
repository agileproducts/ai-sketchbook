# Papers

Playing around with trying to extract bits from academic papers. Uses PDFs from [ArXiv](https://arxiv.org/).

## Requirements

* PDM and Python 3.12.
* An API key for Google Gemini from [Google AI Studio](https://aistudio.google.com/).

## Install

* `pdm install`
* Add a `.env` file with `GEMINI_API_KEY=<your-api-key>`

## Run

```
pdm run python arxiv_dowloader.py 1709-03762
pdm run python convert-paper.py 1709-03762
pdm run python parse-paper.py 1709-03762
```


