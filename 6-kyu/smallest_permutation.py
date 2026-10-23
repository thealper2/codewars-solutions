def min_permutation(n):
    if n == 0:
        return 0

    sign = -1 if n < 0 else 1
    digits = sorted(str(abs(n)))

    if digits[0] == '0':
        for i, d in enumerate(digits):
            if d != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break

    return sign * int(''.join(digits))