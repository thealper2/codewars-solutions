def scramble(strng, array):
    n = len(strng)
    result = [0] * n
    for i in range(n):
        result[array[i]] = strng[i]
        
    return "".join(result)