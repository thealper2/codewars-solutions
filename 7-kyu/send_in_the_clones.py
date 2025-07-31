def clonewars(kata_per_day):
    if kata_per_day == 0:
        return [1, 0]

    num_clones = 2 ** (kata_per_day - 1)
    total_attacks = 0

    for i in range(1, kata_per_day + 1):
        total_attacks += i * (2 ** (kata_per_day - i))

    return [num_clones, total_attacks]
