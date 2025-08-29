def process_data(data):
    prod = 1
    for a, b in data:
        prod *= (a - b)
        
    return prod
