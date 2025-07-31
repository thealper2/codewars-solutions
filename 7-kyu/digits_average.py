import math


def digits_average(n):
    digits = [int(d) for d in str(n)]
    while len(digits) > 1:
        new_digits = []
        for i in range(len(digits) - 1):
            avg = (digits[i] + digits[i + 1]) / 2
            rounded_avg = math.ceil(avg)
            new_digits.append(rounded_avg)
        digits = new_digits

    return digits[0]
