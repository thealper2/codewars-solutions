def split_in_parts(s, part_length): 
    n = len(s)
    result = []
    for i in range(0, n, part_length):
        result.append(s[i:i+part_length])
        
    return ' '.join(result)
