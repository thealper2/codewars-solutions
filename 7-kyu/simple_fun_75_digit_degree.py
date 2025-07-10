def digit_degree(n):
    count = 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
        count += 1
        
    return count
