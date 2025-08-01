def bald(s):
    n = len(s)
    hair_count = s.count('/')
    cleaned = '-' * n
    
    if hair_count > 5:
        return [cleaned, 'Hobo!']
    elif hair_count >= 3:
        return [cleaned, 'Careless!']
    elif hair_count == 2:
        return [cleaned, 'Homer!']
    elif hair_count == 1:
        return [cleaned, 'Unicorn!']
    else:
        return [cleaned, 'Clean!']
