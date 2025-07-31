def calculate_probability(n):
    if n < 2:
        return 0.0

    probability = 1.0
    for i in range(n):
        probability *= (365 - i) / 365

    result = 1 - probability
    return round(result, 2) if result not in (0, 1) else int(result)
