import json
import numpy as np
import mlx.core as mx

data = "../datasets/name-parsing-training-data.md"

with open(data, 'r') as f:
    next(f)
    a = []
    for line in f:
        name, jsonrep = line.strip().split("|")
        b = [name, jsonrep]
        a.append(b)

d = np.array(a)
print(d)