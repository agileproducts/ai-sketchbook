# MLX models

Experimenting with what you can do on a Macbook Air with the [MLX library](https://github.com/ml-explore/mlx).

## Install

Trying to use [PDM](https://pdm-project.org/en/latest/) to manage the pythom mess.

Some of the dependencies won't run on python > 3.12, seemingly.

`pdm install`

The model is downloaded from [Hugging Face](https://huggingface.co). To do this you need to create an account and accept the terms and conditions for the [gemma 2b model](https://huggingface.co/google/gemma-2-2b-it) so that you can access it. 

Add an [access token](https://huggingface.co/docs/hub/en/security-tokens) to be able to download the model.

`pdm run huggingface-cli login`

## Quantize the model

The model is quantized to 4 bits by running:

`pdm run quantize-gemma.py`

By default this saves the quantized model to `mlx_model`. Looks like it takes about 1.5GB of disk space.

I have moved it to ../models/mlx-gemma-2b-it/ so that it can be reused by other parts of the project.

`mv mlx_model ../models/mlx-gemma-2b-it`

## Run

`pdm run run-mlx.py`
