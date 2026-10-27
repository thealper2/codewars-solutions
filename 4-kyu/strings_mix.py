from collections import Counter

def mix(s1, s2):
    c1 = Counter(ch for ch in s1 if 'a' <= ch <= 'z')
    c2 = Counter(ch for ch in s2 if 'a' <= ch <= 'z')
    
    items = []
    for ch in set(c1) | set(c2):
        n1, n2 = c1[ch], c2[ch]
        m = max(n1, n2)
        if m <= 1:
            continue
        if n1 == n2:
            prefix = '=:'
        elif n1 > n2:
            prefix = '1:'
        else:
            prefix = '2:'
            
        items.append(prefix + ch * m)
        
    items.sort(key=lambda s: (-len(s), s))
    return '/'.join(items)