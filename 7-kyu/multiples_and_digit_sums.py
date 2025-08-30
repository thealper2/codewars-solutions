def procedure(i):
    multiples = [num for num in range(0, 101, i)]
    total = 0
    for num in multiples:
        num_sum = 0
        i = 0
        while 10**i <= num:
            d = num // 10**i % 10
            num_sum += d
            i += 1
            
        total += num_sum
            
    return total
