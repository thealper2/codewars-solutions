def cyclops(n):
    bin_n = bin(n)[2:]
    if len(bin_n) % 2 == 0:
        return False
    
    mid = len(bin_n) // 2
    if bin_n[mid] == '0' and bin_n[:mid] == bin_n[mid+1:][::-1]:
        return True
    
    return False
