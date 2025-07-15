import math


def sum_differences_between_products_and_LCMs(pairs):
    total_saving = 0
    for m, n in pairs:
        product = m * n
        gcd = math.gcd(m, n)
        lcm = (m * n) // gcd if gcd != 0 else 0
        saving = product - lcm
        total_saving += saving
        
    return total_saving