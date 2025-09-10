def trim(beard):
    result = []
    for i, row in enumerate(beard):
        if i == len(beard) - 1:
            result.append(['...' for _ in row])
        else:
            result.append(['|' if c == 'J' else c for c in row])
    return result
