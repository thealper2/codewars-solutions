def solve(s):
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated == rotated[::-1]:
            return True
        
    return False
