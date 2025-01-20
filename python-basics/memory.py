import sys
import psutil
import os

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

print(f"Initial memory: {get_memory_usage():.2f} MB")

numbers = []
for i in range(1000001):
    numbers.append(i)

print(f"Memory after creating list: {get_memory_usage():.2f} MB")
print(f"Size of list in memory: {sys.getsizeof(numbers) / 1024:.2f} KB")

print(f"Final memory usage: {get_memory_usage():.2f} MB")