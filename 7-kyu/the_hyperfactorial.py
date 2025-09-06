def hyperfact(num):
    MOD = 1000000007
    result = 1
    for i in range(1, num + 1):
        term = pow(i, i, MOD)
        result = (result * term) % MOD
        
    return result
