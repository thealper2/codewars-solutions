def find_missing_number(numbers):
    n = len(numbers) + 1
    p = n * (n + 1) // 2
    s = sum(numbers)
    r = p - s
    return r