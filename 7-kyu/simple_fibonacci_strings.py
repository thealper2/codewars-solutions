def solve(n):
    f = ['0', '01']
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
        
    return f[n]
