from collections import defaultdict

def ordered_count(inp):
    d = defaultdict(int)
    order = []
    
    for c in inp:
        if c not in d:
            order.append(c)
        
        d[c] += 1
    
    result = [(char, d[char]) for char in order]
    return result
