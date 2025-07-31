import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def pernicious(n):
    if isinstance(n, float):
        if n < 1:
            return "No pernicious numbers"
        n = int(n)
    if n < 1:
        return "No pernicious numbers"

    pernicious_numbers = []
    for num in range(1, n + 1):
        binary = bin(num)[2:]
        digit_sum = sum(int(digit) for digit in binary)
        if is_prime(digit_sum):
            pernicious_numbers.append(num)
    return pernicious_numbers if pernicious_numbers else "No pernicious numbers"
