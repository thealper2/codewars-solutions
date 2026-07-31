def moser():
    n = 1
    while True:
        if n >= 4:
            c4 = n * (n - 1) * (n - 2) * (n - 3) // 24
        else:
            c4 = 0
            
        c2 = n * (n - 1) // 2 if n >= 2 else 0
        yield c4 + c2 + 1
        n += 1
