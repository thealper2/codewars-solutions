def twins(age, distance, velocity):
    total_distance = 2 * distance
    jill_time = total_distance / velocity
    jill_age = age + jill_time
    gamma = (1 - velocity ** 2) ** 0.5
    jack_time = total_distance * gamma / velocity
    jack_age = age + jack_time
    return (round(jack_age, 1), round(jill_age, 1))
