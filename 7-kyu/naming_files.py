def name_file(fmt, nbr, start):
    if nbr <= 0:
        return []
    
    if type(start) != int or type(nbr) != int:
        return []
    
    result = []
    for i in range(nbr):
        result.append(fmt.replace('<index_no>', str(start + i)))
        
    return result
