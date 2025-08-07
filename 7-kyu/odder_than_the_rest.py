def odd_one(arr):
    odd_indices = [i for i, num in enumerate(arr) if num % 2 != 0]
    return odd_indices[0] if len(odd_indices) == 1 else -1
