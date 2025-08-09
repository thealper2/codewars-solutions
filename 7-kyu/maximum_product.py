def adjacent_element_product(array):
    n = len(array)
    max_product = float('-inf')
    
    for i in range(n - 1):
        max_product = max(max_product, array[i] * array[i + 1])
            
    return max_product