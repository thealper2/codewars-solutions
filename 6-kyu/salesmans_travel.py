def travel(r, zipcode):
    streets = []
    numbers = []
    
    for address in r.split(','):
        parts = address.split()
        
        if ' '.join(parts[-2:]) == zipcode:
            numbers.append(parts[0])
            streets.append(' '.join(parts[1:-2]))
            
    return f'{zipcode}:{",".join(streets)}/{",".join(numbers)}' if streets else f'{zipcode}:/' 