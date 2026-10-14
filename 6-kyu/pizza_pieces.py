def max_pizza(cuts):
    return 1 + cuts * (cuts + 1) // 2 if cuts >= 0 else -1