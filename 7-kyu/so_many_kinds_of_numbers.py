digits_not_decimals = []
numeric_not_digits = []

for i in range(0x110000):
    char = chr(i)
    if char.isdigit() and not char.isdecimal():
        digits_not_decimals.append(char)
    if char.isnumeric() and not char.isdigit():
        numeric_not_digits.append(char)
