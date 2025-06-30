def multiple_of_index(arr):
    new_arr = [0] if arr[0] == 0 else []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            new_arr.append(arr[i])

    return new_arr
