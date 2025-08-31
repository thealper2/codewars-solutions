def secret_number(n):
    a = bin(n).count('0') ** 2
    b = bin(n).count('1') ** 2
    if n % 2 == 0:
        return a
    else:
        return b
