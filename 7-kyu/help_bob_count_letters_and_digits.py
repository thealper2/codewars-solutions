def count_letters_and_digits(s):
    return sum(1 for c in s if c.isalpha() or c.isdigit())