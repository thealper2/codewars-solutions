def smallest_transform(num):
    s = str(num)
    min_total = float('inf')
    
    for digit in range(10):
        total = 0
        for c in s:
            d = int(c)
            total += abs(d - digit)

        if total < min_total:
            min_total = total

    return min_total
