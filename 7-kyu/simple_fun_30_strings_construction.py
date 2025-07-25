from collections import Counter


def strings_construction(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    
    min_constructions = float('inf')
    
    for char, count in counter_a.items():
        if char not in counter_b:
            return 0
        constructions = counter_b[char] // count
        if constructions < min_constructions:
            min_constructions = constructions
    
    return min_constructions
