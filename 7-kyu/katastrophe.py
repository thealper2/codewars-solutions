def strong_enough(earthquake, age):
    total = 1
    strength = 1000

    for q in earthquake:
        total *= sum(q)

    for year in range(1, age + 1):
        strength = strength - (strength * 0.01)

    if total < strength:
        return "Safe!"

    return "Needs Reinforcement!"
