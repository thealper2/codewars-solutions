def smallest_product(a):
    min_prod = float('inf')
    for i in a:
        p = i[0]
        for j in i[1:]:
            p *= j
            
        if p < min_prod:
            min_prod = p
            
    return min_prod
