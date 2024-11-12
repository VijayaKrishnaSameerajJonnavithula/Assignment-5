import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Sorted array (randomized):", randomized_quicksort(arr))
