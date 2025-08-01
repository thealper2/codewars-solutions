def mod256_without_mod(number):
    if number < 0:
        while number < 0:
            number += 256
            
        return number
        
    while number >= 256:
        number -= 256
        
    return number
