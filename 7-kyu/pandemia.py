def infected(s):
    people = s.split('X')
    infected = 0
    total = 0
    for p in people:
        total += len(p)
        if '1' in p:
            infected += len(p)

    return (100 * infected) / total if total > 0 else 0
