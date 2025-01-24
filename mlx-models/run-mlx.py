from mlx_lm import load, generate

model, tokenizer = load("../models/mlx-gemma-2b-it")

prompt = "What is a cat?"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

text = generate(model, tokenizer, prompt=prompt, verbose=True)
