def get_number_of_squares(n):
    total = 0
    count = 0
    i = 1
    while total < n:
        total += i * i
        if total < n:
            count += 1
        i += 1
        
    return count
