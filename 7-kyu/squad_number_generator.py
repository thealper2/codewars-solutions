def generate_number(squad, n):
    if n not in squad:
        return n

    possible_numbers = []
    for first_digit in range(1, 10):
        for second_digit in range(1, 10):
            if first_digit + second_digit == n:
                number = first_digit * 10 + second_digit
                possible_numbers.append(number)
                if number not in squad:
                    return number

    return None
