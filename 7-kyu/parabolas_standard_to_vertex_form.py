def get_vertex(a,b,c):
    h = -b / (2 * a)
    k = c - a * h**2
    return [h, k]
