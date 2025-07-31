def calc(arr):
    n = len(arr)
    processed = []
    for i in range(n):
        num = arr[i]
        if num > 0:
            num = num**2

        if (i + 1) % 3 == 0:
            num *= 3

        if (i + 1) % 5 == 0:
            num *= -1

        processed.append(num)

    return sum(processed)
