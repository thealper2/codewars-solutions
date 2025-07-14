def adjust(b, n):
    if n == 0:
        return 0
    if n > 0:
        return n if n % b == 0 else n + (b - n % b)
    else:
        remainder = (-n) % b
        return n if remainder == 0 else n + remainder