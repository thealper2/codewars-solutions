def create_array_of_tiers(n):
    str_n = str(n)
    l = len(str_n)
    result = []
    for i in range(1, l + 1):
        result.append(str_n[0:i])
        
    return result
