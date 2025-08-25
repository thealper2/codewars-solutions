def dollar_to_speech(value):
    if value.startswith('$-'):
        return 'No negative numbers are allowed!'
    
    amount = value[1:]
    dollars, cents = amount.split('.')
    dollars = int(dollars)
    cents = int(cents)
    
    if dollars == 0 and cents == 0:
        return '0 dollars.'
    elif dollars == 1 and cents == 0:
        return '1 dollar.'
    elif dollars == 0 and cents == 1:
        return '1 cent.'
    elif dollars == 0 and cents > 0:
        return f'{cents} cents.'
    elif dollars > 0 and cents == 0:
        return f'{dollars} dollars.' if dollars != 1 else '1 dollar.'
    else:
        dollar_str = 'dollar' if dollars == 1 else 'dollars'
        cent_str = 'cent' if cents == 1 else 'cents'
        return f'{dollars} {dollar_str} and {cents} {cent_str}.'
