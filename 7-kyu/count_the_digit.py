def nb_dig(n, d):
    count = 0
    for i in range(n + 1):
        str_d = str(d)
        str_i = str(i ** 2)
        count += str_i.count(str_d) 
            
    return count
