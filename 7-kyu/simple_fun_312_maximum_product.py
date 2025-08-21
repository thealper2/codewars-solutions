def maximum_product(arr):
    n = len(arr)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= arr[j]
        results.append(product)
    
    max_val = max(results)
    if max_val == 0:
        return min(arr)
    else:
        index = results.index(max_val)
        return arr[index]
