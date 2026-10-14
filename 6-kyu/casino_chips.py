def solve(arr):
    total = sum(arr)
    largest = max(arr)
    return min(total // 2, total - largest)