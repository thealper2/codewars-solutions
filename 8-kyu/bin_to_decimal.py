def bin_to_decimal(inp):
    decimal = 0
    for digit in inp:
        decimal = 2 * decimal + int(digit)
        
    return decimal