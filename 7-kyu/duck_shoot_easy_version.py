def duck_shoot(ammo, aim, ducks):
    successful = int(ammo * aim)
    result = []
    count = 0
    for char in ducks:
        if char == '2' and count < successful:
            result.append('X')
            count += 1
        else:
            result.append(char)
            
    return ''.join(result)
