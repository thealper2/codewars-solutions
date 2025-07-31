def map_population_fit(population, fitness):
    return [ChromosomeWrap(chromosome=c, fitness=fitness(c)) for c in population]
