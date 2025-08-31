def safecracker(start, incs):
    a, b, c = incs
    first = (start - a) % 100
    second = (first + b) % 100
    third = (second - c) % 100
    return (first, second, third)
