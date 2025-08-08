def prev_mult_of_three(n):
    while n:
        if n % 3 == 0:
            return n
        
        n = int(str(n)[:-1]) if n > 10 else 0
        
    return None
