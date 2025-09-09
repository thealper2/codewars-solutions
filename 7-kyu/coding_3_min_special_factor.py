def sc(n): 
    result = []
    bin_n = bin(n)[2:]
    for i in range(1, n + 1):
        if not n % i:
            bin_i = bin(i)[2:]
            if bin_i in bin_n:
                result.append(i)
    
    return result
