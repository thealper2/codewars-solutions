def hist(s):
    errors = ['u', 'w', 'x', 'z']
    result = []
    for error in errors:
        count = s.count(error)
        if count > 0:
            result.append(f'{error}  {count:<6}{"*" * count}')
            
    return '\r'.join(result)