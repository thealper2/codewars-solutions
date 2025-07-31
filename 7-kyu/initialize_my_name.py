def initialize_names(name):
    name = name.split()
    n = len(name)

    for i in range(n):
        if i == 0 or i == n - 1:
            continue

        name[i] = name[i][0].upper() + "."

    return " ".join(name)
