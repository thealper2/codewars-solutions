def closest_multiple_10(i):
    a = i // 10
    b = i % 10
    if b < 5:
        return a * 10
    else:
        return (a + 1) * 10
