def even_numbers_before_fixed(sequence, fixed_element):
    even_count = 0
    for c in sequence:
        if c == fixed_element:
            return even_count
        
        if c % 2 == 0:
            even_count += 1
            
    return -1
