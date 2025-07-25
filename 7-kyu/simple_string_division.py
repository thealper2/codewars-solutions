def solve(st,k):
    n = len(st)
    max_len = n - k
    largest = float('-inf')
    for i in range(n - max_len + 1):
        largest = max(int(st[i:i+max_len]), largest)
        
    return largest
