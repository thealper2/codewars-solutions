def bits_war(numbers):
    odds = 0
    evens = 0

    for n in numbers:
        bits = bin(abs(n)).count('1')
        strength = bits if n > 0 else -bits
        if n % 2 != 0:
            odds += strength
        else:
            evens += strength

    if odds > evens:
        return 'odds win'
    elif evens > odds:
        return 'evens win'
    else:
        return 'tie'