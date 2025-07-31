def battle(x: str, y: str) -> str:
    total = 0

    for c in x:
        if c.isupper():
            total += ord(c) - ord("A") + 1
        else:
            total += (ord(c.upper()) - ord("A") + 1) / 2

    for c in y:
        if c.isupper():
            total -= ord(c) - ord("A") + 1
        else:
            total -= (ord(c.upper()) - ord("A") + 1) / 2

    if total > 0:
        return x
    elif total < 0:
        return y
    else:
        return "Tie!"
