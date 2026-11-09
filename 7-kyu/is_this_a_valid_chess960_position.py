def is_valid(positions):
    bishops = [i for i, c in enumerate(positions) if c == 'B']
    if bishops[0] % 2 == bishops[1] % 2:
        return False
    rooks = [i for i, c in enumerate(positions) if c == 'R']
    king = positions.index('K')
    if not (rooks[0] < king < rooks[1]):
        return False
    return True