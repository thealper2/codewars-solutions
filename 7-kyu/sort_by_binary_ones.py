def sort_by_binary_ones(numList): 
    def key_func(x):
        binary = bin(x)[2:]
        ones = binary.count('1')
        length = len(binary)
        return (-ones, length, x)
    
    return sorted(numList, key=key_func)
