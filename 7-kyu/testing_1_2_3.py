def number(lines):
    return [f'{i}: {lines[i - 1]}' for i in range(1, len(lines) + 1)]
