def remove(s):
    end_excl = 0
    for char in reversed(s):
        if char == '!':
            end_excl += 1
        else:
            break
    
    result = s.replace('!', '') + ('!' * end_excl)
    return result
