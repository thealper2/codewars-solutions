def get_issuer(number):
    number = str(number)
    n = len(number)
    
    if n == 15 and (number.startswith('34') or number.startswith('37')):
        return 'AMEX'
    elif n == 16 and number.startswith('6011'):
        return 'Discover'
    elif n == 16 and (
        number.startswith('51')
        or number.startswith('52')
        or number.startswith('53')
        or number.startswith('54')
        or number.startswith('55')
    ):
        return 'Mastercard'
    elif (n == 13 or n == 16) and (number.startswith('4')):
        return 'VISA'
    else:
        return 'Unknown'
