def tower_combination(n):
    if n == 1:
        return 1
    else:
        return n * tower_combination(n - 1)
