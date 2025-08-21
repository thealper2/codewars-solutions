def painted_faces(length, n):
    if length == 0:
        return 0
    if n == 0:
        return max(0, (length - 2) ** 3)
    elif n == 1:
        return 6 * max(0, (length - 2) ** 2) if length >= 2 else (1 if length == 1 and n == 6 else 0)
    elif n == 2:
        return 12 * max(0, length - 2)
    elif n == 3:
        return 8 if length >= 2 else 0
    elif n == 6:
        return 1 if length == 1 else 0
    else:
        return 0
