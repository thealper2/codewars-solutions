def max_product(a):
    first = float('-inf')
    second = float('-inf')
    for item in a:
        if item > first:
            second = first
            first = item
        elif item > second:
            second = item
            
    return first * second
