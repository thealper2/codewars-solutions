def solution(stones):
    removals = 0
    i = 0
    n = len(stones)
    while i < n - 1:
        if stones[i] == stones[i+1]:
            removals += 1
            
        i += 1
    return removals