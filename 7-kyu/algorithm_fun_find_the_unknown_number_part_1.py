def find_unknown_number(x,y,z):
    n = 1
    while True:
        if n % 3 == x and n % 5 == y and n % 7 == z:
            return n
        
        n += 1
