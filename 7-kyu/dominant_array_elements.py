def solve(arr):
    n = len(arr)
    max_so_far = arr[-1]
    result = [max_so_far]

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_so_far and arr[i] not in result:
            max_so_far = arr[i]
            result.append(max_so_far)

    return result[::-1]
