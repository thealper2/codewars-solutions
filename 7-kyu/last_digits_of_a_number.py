def solution(n,d):
    if d <= 0:
        return []
    
    s = str(n)
    if d > len(s):
        return [int(c) for c in s]
    
    return [int(c) for c in s[-d:]]
