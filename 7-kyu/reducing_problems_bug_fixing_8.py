from functools import reduce


def calculate_total(t1, t2):
    t1_score = reduce(lambda a, b: a + b, t1, 0) if t1 else 0
    t2_score = reduce(lambda a, b: a + b, t2, 0) if t2 else 0
    return t1_score > t2_score
