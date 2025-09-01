def solve(s):
    n = len(s)
    diff = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            diff += 1
            
    return diff == 1 or (diff == 0 and n % 2 == 1)
