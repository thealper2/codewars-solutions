def capital(capitals): 
    result = []
    for item in capitals:
        place = item.get('state') or item.get('country')
        capital = item.get('capital')
        if place and capital:
            result.append(f"The capital of {place} is {capital}")
    return result
