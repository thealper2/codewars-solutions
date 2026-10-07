def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []
    
    def to_int(arr):
        if not arr:
            return 0
        sign = -1 if arr[0] < 0 else 1
        s = ''.join(str(abs(x)) for x in arr)
        return sign * int(s)
    
    total = to_int(array1) + to_int(array2)
    s = str(abs(total))
    first = -int(s[0]) if total < 0 else int(s[0])
    return [first] + [int(d) for d in s[1:]]