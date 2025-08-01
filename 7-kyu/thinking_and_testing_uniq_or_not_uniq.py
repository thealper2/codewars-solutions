def testit(a, b):
    a = list(set(a)) + list(set(b))
    return sorted(a)
