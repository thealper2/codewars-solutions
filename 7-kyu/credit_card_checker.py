def valid_card(card):
    cleaned = "".join(filter(str.isdigit, card))
    digits = [int(digit) for digit in cleaned]
    transformed_digits = digits.copy()
    for i in range(len(transformed_digits) - 2, -1, -2):
        doubled = transformed_digits[i] * 2
        transformed_digits[i] = doubled - 9 if doubled > 9 else doubled

    return sum(transformed_digits) % 10 == 0
