def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    a1 = sorted(a1, key=lambda x: len(x))
    a2 = sorted(a2, key=lambda x: len(x))
    return max(
        abs(len(a1[0]) - len(a2[-1])),
        abs(len(a1[-1]) - len(a2[0]))
    )
