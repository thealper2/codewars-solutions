def sentence(lst):
    pairs = []
    for d in lst:
        for k, v in d.items():
            pairs.append((int(k), v))
    
    pairs.sort(key=lambda x: x[0])
    return ' '.join(v for k, v in pairs)
