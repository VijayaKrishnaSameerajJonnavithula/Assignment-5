import time
import random
from Quicksort import quicksort
from Randomsort import randomized_quicksort


# Function to time the execution of a sorting algorithm
def time_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

# Generate different input types
input_sizes = [100, 1000, 5000, 10000]
input_types = {
    "random": lambda size: [random.randint(0, 10000) for _ in range(size)],
    "sorted": lambda size: list(range(size)),
    "reverse_sorted": lambda size: list(range(size, 0, -1))
}

# Compare deterministic and randomized Quicksort
for size in input_sizes:
    for input_type, generator in input_types.items():
        arr = generator(size)
        time_deterministic = time_sorting_algorithm(quicksort, arr)
        time_randomized = time_sorting_algorithm(randomized_quicksort, arr)
        print(f"Size: {size}, Type: {input_type}")
        print(f"  Deterministic Quicksort: {time_deterministic:.5f} sec")
        print(f"  Randomized Quicksort: {time_randomized:.5f} sec")
