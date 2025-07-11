def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        first_part = ' '.join(arr[:i])
        second_part = ' '.join(arr[i:])
        result.append((first_part, second_part))
    return result
