
def next_id(arr):
    sorted_arr = list(set(sorted(arr)))
    new_arr = []
    for i in range(len(sorted_arr)):
        if sorted_arr[i] >= 0:
            new_arr.append(sorted_arr[i])

    for i in range(len(new_arr)):
        if new_arr[i] != i:
            return i

    return len(new_arr)
