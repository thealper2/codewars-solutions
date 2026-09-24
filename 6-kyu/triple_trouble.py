def triple_double(num1, num2):
    s1 = str(num1)
    s2 = str(num2)

    for d in '0123456789':
        if d * 3 in s1 and d * 2 in s2:
            return 1

    return 0