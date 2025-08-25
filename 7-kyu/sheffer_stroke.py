def NOT(a):
    return sheffer(a, a)

def AND(a, b):
    return NOT(sheffer(a, b))

def OR(a, b):
    return sheffer(NOT(a), NOT(b))
