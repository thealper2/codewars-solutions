def crossover(chromosome1, chromosome2, index):
    temp = chromosome1
    chromosome1 = chromosome1[:index] + chromosome2[index:]
    chromosome2 = chromosome2[:index] + temp[index:]
    return [chromosome1, chromosome2]