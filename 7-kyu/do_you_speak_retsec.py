def reverse_by_center(s):
    n = len(s) // 2
    if len(s) % 2 == 0:
        return s[n:] + s[:n]
    
    return s[n+1:] + s[n] + s[:n]