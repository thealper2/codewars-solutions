def minimum_percentage(foods):
    total = sum(foods)
    n = len(foods)
    min_all = total - (n - 1) * 100
    return max(0, min_all)
