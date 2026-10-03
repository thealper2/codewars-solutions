def balance(left, right):
    ls = left.count('!') * 2 + left.count('?') * 3
    rs = right.count('!') * 2 + right.count('?') * 3
    if ls < rs:
        return 'Right'
    elif rs < ls:
        return 'Left'
    else:
        return 'Balance'