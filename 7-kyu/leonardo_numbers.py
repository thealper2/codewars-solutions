def leonardo_numbers(n, L0, L1, add) :
    leonardo_numbers = [L0, L1]
    for i in range(2, n):
        l = leonardo_numbers[i - 1] + leonardo_numbers[i - 2] + add
        leonardo_numbers.append(l)
    
    return leonardo_numbers