def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            return False

    return True

def total(arr):
    if not arr or len(arr) < 2:
        return 0

    idx = 0
    n = len(arr)
    result = 0
    for i in range(n):
        if is_prime(i):
            result += arr[i]

    return result