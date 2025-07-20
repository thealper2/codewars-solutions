def factors(integer, limit):
    return [i for i in range(limit, integer + 1) if integer % i == 0]