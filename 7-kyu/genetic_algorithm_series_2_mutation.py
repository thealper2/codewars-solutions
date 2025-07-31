import random


def mutate(chromosome, p):
    mutated = []
    for bit in chromosome:
        if random.random() < p:
            mutated.append("1" if bit == "0" else "0")
        else:
            mutated.append(bit)
    return "".join(mutated)
