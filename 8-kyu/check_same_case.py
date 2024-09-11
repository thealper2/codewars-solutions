def same_case(a, b):
    ord_a = ord(a)
    ord_b = ord(b)
    if not a.isalpha() or not b.isalpha():
        return -1

    if 64 < ord_a < 97 and 64 < ord_b < 97:
        return 1
    elif 96 < ord_a < 123 and 96 < ord_b < 123:
        return 1
    else:
        return 0
