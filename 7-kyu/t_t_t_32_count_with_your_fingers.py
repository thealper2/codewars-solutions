def which_finger(n):
    d = {
        'a': 'Thumb',
        'b': 'Index finger',
        'c': 'Middle finger',
        'd': 'Ring finger',
        'e': 'Little finger'
    }
    pattern = ['a','b','c','d','e','d','c','b']
    return d[pattern[(n - 1) % 8]]
