def solution(n,b):
    if b == 0:
        return []
    
    max_num = (1 << n) - 1
    result = []
    for num in range(max_num + 1):
        if num & b:
            result.append(num)
    
    return result
