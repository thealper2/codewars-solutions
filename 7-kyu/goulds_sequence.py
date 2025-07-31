def gould():
    n = 0
    while True:
        yield bin(n).count("1")
        n += 1
