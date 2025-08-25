def base_finder(seq):
    unique_digits = set()
    for num in seq:
        for digit in num:
            unique_digits.add(digit)
            
    return len(unique_digits)
