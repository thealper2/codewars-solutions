import collections
import numpy as np

def can_traverse(x):
    rows = len(x)
    cols = len(x[0])
    h = [sum(x[r][c] for r in range(rows)) for c in range(cols)]
    if h[0] > 1:
        return False

    for i in range(cols - 1):
        if abs(h[i + 1] - h[i]) > 1:
            return False

    return True
