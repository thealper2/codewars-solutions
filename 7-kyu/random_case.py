import random


def random_case(x):
    return "".join(random.choice([c.upper(), c.lower()]) for c in x)
