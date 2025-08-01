def int_rac(n, guess):
    count = 1
    current_guess = guess
    
    while True:
        new_guess = (current_guess + n // current_guess) // 2
        if abs(new_guess - current_guess) < 1:
            break
            
        current_guess = new_guess
        count += 1
        
    return count
