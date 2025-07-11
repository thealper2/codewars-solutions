def sc(width, length, gap):
    perimeter = width + width + length + length - 4
    if perimeter % (gap + 1) != 0:
        return 0
    else:
        return perimeter / (gap + 1)
