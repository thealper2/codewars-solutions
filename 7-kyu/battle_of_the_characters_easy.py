def battle(x, y):
    power1 = sum(ord(c) - ord('A') + 1 for c in x)
    power2 = sum(ord(c) - ord('A') + 1 for c in y)
    
    if power1 > power2:
        return x
    elif power2 > power1:
        return y
    else:
        return "Tie!"
