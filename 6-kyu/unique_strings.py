import math
from collections import Counter


def uniq_count(s):
    new_s = s.upper()
    freq = Counter(new_s)
    n = len(new_s)
    numerator = math.factorial(n)
    denominator = 1
    for f in freq.values():
        denominator *= math.factorial(f)
        
    return numerator // denominator
