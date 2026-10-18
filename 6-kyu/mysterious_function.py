def get_num(n):
    holes = {'0': 1, '6': 1, '9': 1, '8': 2}
    return sum(holes.get(d, 0) for d in str(n))