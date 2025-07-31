def total(arr):
    while len(arr) > 1:
        temp = []
        for i in range(len(arr) - 1):
            temp.append(arr[i] + arr[i + 1])

        arr = temp

    return arr[0]
