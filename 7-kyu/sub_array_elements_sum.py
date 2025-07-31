def elements_sum(arr, d=0):
    n = len(arr)
    total = 0
    for i in range(n, 0, -1):
        outer_index = n - i
        if len(arr[outer_index]) > i - 1:
            total += arr[outer_index][i - 1]
        else:
            total += d

    return total
