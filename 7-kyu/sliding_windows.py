def window(lngth, offst, lst):
    n = len(lst)
    result = []

    for i in range(0, n - lngth + 1, offst):
        result.append(lst[i : i + lngth])

    return result
