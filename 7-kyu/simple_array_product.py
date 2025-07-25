from itertools import product
from functools import reduce

def solve(arr):
    combinations = product(*arr)
    max_product = float('-inf')
    for comb in combinations:
        current_product = reduce(lambda x, y : x * y, comb)
        max_product = max(max_product, current_product)

    return max_product