def sum_times_tables(table, a, b):
    if not table:
        return 0

    total = 0
    for i in range(a, b + 1):
        total += sum([i * t for t in table])

    return total
