def is_lucky(n):
    i = 0
    total = 0
    while 10**i <= n:
        d = n//10**i % 10
        total += d
        i += 1
        
    return total == 0 or total % 9 == 0
