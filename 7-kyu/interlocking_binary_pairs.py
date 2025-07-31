def interlockable(a, b):
    a_binary = []
    b_binary = []

    while a >= 1 and b >= 1:
        a_binary.append(a % 2)
        a //= 2

    while b >= 1:
        b_binary.append(b % 2)
        b //= 2

    n = min(len(a_binary), len(b_binary))

    for a_, b_ in zip(a_binary[:n], b_binary[:n]):
        if a_ == 1 and b_ == 1:
            return False

    return True
