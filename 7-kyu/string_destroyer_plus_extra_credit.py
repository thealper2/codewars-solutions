def destroyer(input_sets):
    d = [chr(i) for i in range(97, 123)]
    for input_ in input_sets:
        for c in input_:
            if c in d:
                d[d.index(c)] = '_'
                
    return ' '.join(d)
