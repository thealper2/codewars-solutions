from collections import Counter

def added_char(s1, s2):  
    f1 = Counter(s1)
    f2 = Counter(s2)
    for k, v in f1.items():
        f2[k] = f2.get(k, 0) - v
        if f2[k] == 0:
            del f2[k]
    
    return list(f2.keys())[0]