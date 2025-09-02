from collections import defaultdict


def two_by_two(animals):
    if not animals:
        return False
    
    count = defaultdict(int)
    for animal in animals:
        count[animal] += 1
        
    result = {}
    for animal, cnt in count.items():
        if cnt >= 2:
            result[animal] = 2
            
    return result
