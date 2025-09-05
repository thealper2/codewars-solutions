def num_of_open_lockers(n):
    i = 0
    while (i + 1) ** 2 <= n:
        i += 1
        
    return i
