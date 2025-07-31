def solve(arr):
    arr.sort()
    result = []
    l, r = 0, len(arr) - 1

    while l <= r:
        if l != r:
            result.append(arr[r])
            result.append(arr[l])
        else:
            result.append(arr[l])

        l += 1
        r -= 1

    return result
