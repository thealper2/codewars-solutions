import math

def am_i_wilson(n):
    if n < 2:
        return False

    factorial_mod = math.factorial(n - 1) % (n * n)
    return factorial_mod == (n * n - 1)
