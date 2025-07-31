def make_valley(arr):
    if not arr:
        return []

    arr.sort()
    result = [arr[0]]
    n = len(arr)
    l = False
    if n % 2 == 0:
        for i in range(1, n):
            if l:
                result.append(arr[i])
            else:
                result.insert(0, arr[i])

            l = not l

    else:
        for i in range(1, n):
            if l:
                result.insert(0, arr[i])
            else:
                result.append(arr[i])

            l = not l
    return result
