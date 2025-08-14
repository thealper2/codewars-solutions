def recaman(n):
    if n == 0:
        return 0
    sequence = [0]
    seen = {0}
    for i in range(1, n + 1):
        prev = sequence[-1]
        next_term = prev - i
        if next_term > 0 and next_term not in seen:
            sequence.append(next_term)
            seen.add(next_term)
        else:
            next_term = prev + i
            sequence.append(next_term)
            seen.add(next_term)
    return sequence[n]
