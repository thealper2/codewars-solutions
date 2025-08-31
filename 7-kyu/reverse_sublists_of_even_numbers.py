def rev_sub(arr):
    result = []
    i = 0
    n = len(arr)
    
    while i < n:
        if arr[i] % 2 == 0:
            j = i
            while j < n and arr[j] % 2 == 0:
                j += 1
    
            segment = arr[i:j]
            result.extend(segment[::-1])
            i = j
        else:
            result.append(arr[i])
            i += 1
    return result
