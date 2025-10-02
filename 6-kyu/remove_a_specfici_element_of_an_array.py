def select_subarray(arr):
    n = len(arr)
    min_q = float('inf')
    result = []
    
    for i in range(n):
        sub_arr = arr[:i] + arr[i+1:]
        sub_sum = sum(sub_arr)
        if sub_sum == 0:
            continue
            
        sub_product = 1
        for num in sub_arr:
            sub_product *= num
            
        q = abs(sub_product / sub_sum)
        if abs(q - min_q) < 1e-12:
            result.append([i, arr[i]])
        elif q < min_q:
            min_q = q
            result = [[i, arr[i]]]
            
    return result[0] if len(result) == 1 else sorted(result)
