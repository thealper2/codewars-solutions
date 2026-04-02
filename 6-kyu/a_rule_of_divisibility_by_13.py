def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4]
    prev_result = None
    current = n
    
    while prev_result != current:
        prev_result = current
        digits = str(current)
        total = 0
        for i, digit_char in enumerate(reversed(digits)):
            seq_index = i % len(sequence)
            digit = int(digit_char)
            total += digit * sequence[seq_index]
            
        current = total
        
    return current
