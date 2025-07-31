def equalize(arr):
    if not arr:
        return []

    first = arr[0]
    result = []
    for num in arr:
        diff = num - first
        if diff >= 0:
            result.append(f"+{diff}")
        else:
            result.append(f"{diff}")

    return result
