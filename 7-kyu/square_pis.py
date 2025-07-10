import math


def square_pi(digits):
    pi_digits = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    selected_digits = pi_digits[:digits]
    sum_squares = sum(int(d)**2 for d in selected_digits)
    
    sqrt_sum = math.isqrt(sum_squares)
    if sqrt_sum * sqrt_sum == sum_squares:
        return sqrt_sum
    else:
        return sqrt_sum + 1
