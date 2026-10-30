def next_bigger(n):
    digits = list(str(n))
    L = len(digits)

    i = L - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return -1

    j = L - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = digits[i + 1:][::-1]
    return int(''.join(digits))