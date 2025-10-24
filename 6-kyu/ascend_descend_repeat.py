def ascend_descend(length, minimum, maximum):
    if maximum < minimum or length == 0:
        return ""
    
    if minimum == maximum:
        return str(minimum) * length
    
    result = []
    current = minimum
    direction = 1
    
    while len("".join(result)) < length:
        num_str = str(current)
        result.append(num_str)
        
        if len("".join(result)) > length:
            break
            
        if current == maximum:
            direction = -1
        elif current == minimum:
            direction = 1
        
        current += direction
    
    final_string = "".join(result)
    return final_string[:length]
