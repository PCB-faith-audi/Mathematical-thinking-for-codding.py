def randomized_quicksort(arr):
    """Sort the array using randomized quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Generate a random unsorted list
unsorted_array = [random.randint(1, 100) for _ in range(10)]
print("Unsorted array:", unsorted_array)
print("Sorted:", randomized_quicksort(unsorted_array))