def first_n_smallest(arr, n):
    if n <= 0:
        return []

    idx = sorted(range(len(arr)), key=lambda i: (arr[i], i))[:n]
    idx.sort()
    return [arr[i] for i in idx]