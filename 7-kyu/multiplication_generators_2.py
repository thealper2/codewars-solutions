def generator(a):
    b = 1
    while True:
        c = a * b
        yield f'{a} x {b} = {c}'
        b += 1
