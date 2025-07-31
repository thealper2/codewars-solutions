def passed(lst):
    n = len(lst)
    total = 0

    for item in lst:
        if item <= 18:
            total += item
        else:
            n -= 1

    if not n:
        return "No pass scores registered."

    return round(total / n)
