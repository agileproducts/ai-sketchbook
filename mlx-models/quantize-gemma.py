from mlx_lm import convert

repo = "google/gemma-2-2b-it"

convert(repo, quantize=True)
