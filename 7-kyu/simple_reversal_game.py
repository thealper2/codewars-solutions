def solve(n,k):
    if n == 1:
        return 0
    
    if k < n // 2:
        return 2 * k + 1
    
    else:
        return 2 * (n - k - 1)
