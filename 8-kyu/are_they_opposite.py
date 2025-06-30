def is_opposite(s1, s2):
    if s1 == s2:
        return False

    for l1, l2 in zip(s1, s2):
        if l1 == l2:
            return False

    return True
