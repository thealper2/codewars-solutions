def gimme_the_letters(sp):
    l, r = map(ord, sp.split('-'))
    return ''.join([chr(i) for i in range(l, r + 1)])
