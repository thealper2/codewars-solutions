def mul37(num):
    for a in range(0, 1001):
        for b in range(0, 1001):
            if 3*a + 7*b == num:
                return f"3 * {a} + 7 * {b}"
