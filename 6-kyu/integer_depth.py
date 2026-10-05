def compute_depth(n):
    depth = 0
    numbers = set()
    i = 1
    while len(numbers) != 10:
        p = 0
        num = i * n
        while 10**p <= num:
            d = num // 10**p % 10
            numbers.add(d)
            p += 1
        
        i += 1
        
    return i - 1