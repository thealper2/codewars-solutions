import math

def merge_ratios(ratio1,ratio2):
    a1, b1 = map(int, ratio1.split(':'))
    b2, c2 = map(int, ratio2.split(':'))
    lcm_b = abs(b1 * b2) // math.gcd(b1, b2)
    scale1 = lcm_b // b1
    scale2 = lcm_b // b2
    a = a1 * scale1
    b = lcm_b
    c = c2 * scale2
    gcd_all = math.gcd(math.gcd(a, b), c)
    a //= gcd_all
    b //= gcd_all
    c //= gcd_all
    return f"{a}:{b}:{c}"