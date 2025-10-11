def prime_string(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            if s == s[:i] * (n // i):
                return False
            
    return True
