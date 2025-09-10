from collections import defaultdict

def separate_types(seq): 
    types = defaultdict(list)
    for item in seq:
        types[type(item)].append(item)
        
    return types
