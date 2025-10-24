def power(n):
    MOD = 10 ** 10
    total = 0
    for i in range(1, n + 1):
        total = (total + pow(i, i, MOD)) % MOD
        
    return str(total)
