def validate(n):
    digits = [int(d) for d in str(n)]
    digits.reverse()
    total = 0

    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9

        total += d

    return total % 10 == 0