def array_packing(arr):
    arr_s = ''.join([bin(item)[2:].zfill(8) for item in arr[::-1]])
    return int(arr_s, 2)