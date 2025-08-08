def power_of_two(x):
    i = 0
    while 2 ** i < x:
        i += 1
        
    return 2 ** i == x
