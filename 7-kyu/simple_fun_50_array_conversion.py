def array_conversion(arr):
    iteration = 1
    while len(arr) > 1:
        new_arr = []
        if iteration % 2 == 1:
            for i in range(0, len(arr), 2):
                if i + 1 < len(arr):
                    new_arr.append(arr[i] + arr[i + 1])
                else:
                    new_arr.append(arr[i])
        else:
            for i in range(0, len(arr), 2):
                if i + 1 < len(arr):
                    new_arr.append(arr[i] * arr[i + 1])
                else:
                    new_arr.append(arr[i])
        arr = new_arr
        iteration += 1
    return arr[0]
