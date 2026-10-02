def fold_array(array, runs):
    arr = list(array)
    for _ in range(runs):
        n = len(arr)
        half = n // 2
        left = arr[:half]
        right = arr[n - half:]
        new_arr = [left[i] + right[half - 1 - i] for i in range(half)]
        if n % 2 == 1:
            new_arr.append(arr[half])

        arr = new_arr

    return arr