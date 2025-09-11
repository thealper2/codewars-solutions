def is_in_middle(sequence):
    n = len(sequence)
    for idx in range(n):
        if sequence[idx:idx+3] == 'abc':
            l = len(sequence[:idx])
            r = len(sequence[idx+3:])
            if abs(l - r) <= 1:
                return True

    return False
