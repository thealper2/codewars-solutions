def min_and_max(l, d, x):
    min_n = d
    max_m = l
    
    for num in range(l, d + 1):
        if sum(int(digit) for digit in str(num)) == x:
            if num < min_n:
                min_n = num
            if num > max_m:
                max_m = num
                
    return [min_n, max_m]
