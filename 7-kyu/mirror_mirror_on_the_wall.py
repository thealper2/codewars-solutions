def mirror(data: list) -> list:
    data_sorted = sorted(data)
    data_mutate = data_sorted[::-1][1:]
    return data_sorted + data_mutate
