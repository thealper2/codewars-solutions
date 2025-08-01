def search(budget, prices):
    result = []
    for price in prices:
        if price <= budget:
            result.append(price)
            
    return ','.join(map(str, sorted(result)))
