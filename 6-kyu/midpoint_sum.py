def midpoint_sum(ints):
    n = len(ints)
    if n == 0:
        return -1

    total = sum(ints)
    left_sum = 0

    for i in range(n):
        right_sum = total - left_sum - ints[i]
        if 0 < i < n - 1 and left_sum == right_sum:
            return i

        left_sum += ints[i]

    return -1