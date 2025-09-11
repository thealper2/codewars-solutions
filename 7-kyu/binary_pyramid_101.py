def binary_pyramid(m,n):
    result = 0
    for i in range(m, n + 1):
        bin_i = bin(i)[2:]
        result += int(bin_i)
    
    return bin(result)[2:]
