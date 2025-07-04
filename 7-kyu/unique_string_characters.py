def solve(a,b):
    result = ""
    
    for c in a:
        if c not in b:
            result += c
            
    for c in b:
        if c not in a:
            result += c
            
    return result
