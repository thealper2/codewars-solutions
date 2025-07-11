import math


def mn_lcm(m, n):
    if m > n:
        m, n = n, m
        
    current_lcm = 1
    for num in range(m, n + 1):
        current_lcm = (current_lcm * num) // math.gcd(current_lcm, num)
    
    return current_lcm
