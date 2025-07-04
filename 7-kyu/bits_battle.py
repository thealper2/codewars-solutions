def bits_battle(numbers):
    odds_count = 0
    evens_count = 0
    
    for number in numbers:
        if number == 0:
            continue
        binary = bin(number)[2:]
        if number % 2 == 1:
            odds_count += binary.count('1')
        else:
            evens_count += binary.count('0')
    
    if odds_count > evens_count:
        return "odds win"
    elif evens_count > odds_count:
        return "evens win"
    else:
        return "tie"
