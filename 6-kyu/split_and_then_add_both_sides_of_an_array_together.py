def split_and_add(arr, n):
    for _ in range(n):
        if len(arr) <= 1:
            break
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        size = max(len(left), len(right))
        left = [0] * (size - len(left)) + left
        right = [0] * (size - len(right)) + right
        arr = [a + b for a, b in zip(left, right)]

    return arr