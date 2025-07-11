def pages_numbering_with_ink(current, number_of_digits):
    while number_of_digits >= len(str(current)):
        number_of_digits -= len(str(current))
        current += 1
    return current - 1
