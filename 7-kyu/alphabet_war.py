def alphabet_war(fight):
    l, r = 0, 0
    ld = {"w": 4, "p": 3, "b": 2, "s": 1}
    rd = {"m": 4, "q": 3, "d": 2, "z": 1}
    for f in fight:
        l += ld.get(f, 0)
        r += rd.get(f, 0)

    if l > r:
        return "Left side wins!"
    elif l < r:
        return "Right side wins!"
    else:
        return "Let's fight again!"
