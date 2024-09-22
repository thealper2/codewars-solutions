def triple_trouble(one, two, three):
    result = ""
    for a, b, c in zip(one, two, three):
        result += a + b + c
        
    return result