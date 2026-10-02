def triangle_type(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides

    if x + y <= z:
        return 0

    lhs = z * z
    rhs = x * x + y * y


    if lhs == rhs:
        return 2
    elif lhs < rhs:
        return 1
    else:
        return 3