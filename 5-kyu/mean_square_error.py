def solution(array_a, array_b):
    sub = 0
    n = len(array_a)
    for a, b in zip(array_a, array_b):
        sub += (b - a) ** 2
        
    return sub / n