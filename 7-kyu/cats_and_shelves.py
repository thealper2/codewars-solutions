def solution(start, finish):  
    distance = finish - start
    jumps = distance // 3
    remainder = distance % 3
    if remainder == 1:
        jumps += 1
    elif remainder == 2:
        jumps += 2
        
    return jumps
