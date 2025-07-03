def is_orthogonal(u, v): 
    dot_product = sum(a * b for a, b in zip(u, v))
    return dot_product == 0