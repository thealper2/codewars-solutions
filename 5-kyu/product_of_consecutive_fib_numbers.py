def product_fib(_prod):
    a, b = 0, 1
    while a * b <= _prod:
        if a * b == _prod:
            return [a, b, True]

        a, b = b, a + b

    return [a, b, False]