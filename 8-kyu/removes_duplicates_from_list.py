def distinct(seq):
    f = []
    for val in seq:
        if val not in f:
            f.append(val)
            
    return f