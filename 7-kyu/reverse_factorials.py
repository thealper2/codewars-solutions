def reverse_factorial(num):
    s = 1
    c = 1
    while s < num:
        c += 1
        s *= c
        
    if s != num:
        return "None"
    
    return f"{c}!"
