import math
from collections import Counter

def entropy(message: str) -> float:
    message = ''.join(c for c in message if c != ' ')
    n = len(message)
    freq = Counter(message)
    result = -sum((v / n) * math.log2((v / n)) for v in freq.values())
    return result