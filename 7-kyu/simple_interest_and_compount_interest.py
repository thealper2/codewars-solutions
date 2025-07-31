def interest(p, r, n):
    simple_total = round(p + p * r * n)
    compound_total = round(p * (1 + r) ** n)
    return [simple_total, compound_total]
