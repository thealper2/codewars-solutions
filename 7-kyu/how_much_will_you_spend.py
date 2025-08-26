def get_total(costs, items, tax):
    total = 0
    for item in items:
        total += costs.get(item, 0)
        
    result = total + (total * tax)
    return round(result, 2)
