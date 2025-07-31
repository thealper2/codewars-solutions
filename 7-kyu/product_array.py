def product_array(numbers):
    n = len(numbers)
    if n == 0:
        return []

    prod = [1] * n
    prefix = 1
    for i in range(n):
        prod[i] = prefix
        prefix *= numbers[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        prod[i] *= suffix
        suffix *= numbers[i]

    return prod
