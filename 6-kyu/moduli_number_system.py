from math import gcd
from functools import reduce

def from_nb_2_str(n, modsys):
    for i in range(len(modsys)):
        for j in range(i + 1, len(modsys)):
            if gcd(modsys[i], modsys[j]) != 1:
                return 'Not applicable'
            
    product = reduce(lambda a, b: a * b, modsys, 2)
    if product <= n:
        return 'Not applicable'
    
    residues = [str(n % m) for m in modsys]
    return '-' + '--'.join(residues) + '-'