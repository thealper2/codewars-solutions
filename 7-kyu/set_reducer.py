def set_reducer(arr):
    def reduce_step(a):
        result = []
        n = len(a)
        i = 0
        while i < n:
            count = 1
            while i < n - 1 and a[i] == a[i+1]:
                count += 1
                i += 1
            if count == 1:
                result.append(1)
            else:
                result.append(count)
            i += 1
        return result
    
    while len(arr) > 1:
        arr = reduce_step(arr)
    return arr[0]
