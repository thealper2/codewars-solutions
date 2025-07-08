import random


def generate(length):
    chromosome = []
    for _ in range(length):
        bit = random.choice(['0', '1'])
        chromosome.append(bit)
        
    return ''.join(chromosome)