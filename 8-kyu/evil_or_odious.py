def evil(n):
    b = ""
    c = 0
    while n:
        b += str(n & 1)
        if n & 1:
            c += 1
            
        n = n >> 1
        
    return "It's Odious!" if c % 2 != 0 else "It's Evil!"