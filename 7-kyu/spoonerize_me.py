def spoonerize(words):
    a, b = words.split()
    a, b = b[0] + a[1:], a[0] + b[1:]
    return ' '.join([a, b])
