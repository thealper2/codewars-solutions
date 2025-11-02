def validate_euro(serial):
    letter1 = ord(serial[0]) - ord('A') + 1
    letter2 = ord(serial[1]) - ord('A') + 1
    digit_sum = sum(int(d) for d in serial[2:])
    total = letter1 + letter2 + digit_sum
    while total >= 10:
        total = sum(int(d) for d in str(total))
        
    return total == 7
