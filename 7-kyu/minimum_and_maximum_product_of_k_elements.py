from itertools import combinations
from functools import reduce

def find_min_max_product(arr, k):
    n = len(arr)
    if k > n:
        return
    
    max_product = float('-inf')
    min_product = float('inf')
    for comb in combinations(arr, k):
        prod = reduce(lambda x, y: x * y, comb)
        max_product = max(max_product, prod)
        min_product = min(min_product, prod)
        
    return (min_product, max_product)
    
