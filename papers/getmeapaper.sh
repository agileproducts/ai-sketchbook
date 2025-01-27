#! /bin/zsh

echo "fetching $1"
pdm run python arxiv-downloader.py "$1"
echo "converting to markdown"
pdm run python convert-paper.py "$1"
echo "doing LLM stuff.."
pdm run python parse-paper-gemma.py "$1"