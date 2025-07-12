import random


def find_random_seed(lst):
    for seed in range(0, 10000):
        random.seed(seed)
        generated = [random.randint(0, 100) for _ in range(10)]
        if generated == lst:
            return seed
        
    return -1