def get_strings(city):
    seen = set(' ')
    city = city.lower()
    result = []
    for c in city:
        if c not in seen:
            seen.add(c)
            result.append(c + ':' + '*' * city.count(c))
            
    return ','.join(result)
        
