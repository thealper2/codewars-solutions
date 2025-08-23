def find_children(santas_list, children):
    result = []
    for c in santas_list:
        if c in children:
            result.append(c)
            
    result = sorted(result)
    return result
