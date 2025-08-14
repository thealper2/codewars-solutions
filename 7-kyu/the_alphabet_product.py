from itertools import combinations



def alphabet(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    for candidate in combinations(numbers, 4):
        A, B, C, D = candidate
        if A >= B or B >= C or C >= D:
            continue 
        
        products = {A*B, B*C, C*D, D*A}
        if products.issubset(set(numbers)):
            return D
        
    return -1 
