def solution(to_currency,values):
    rate = 1.1363636
    result = []
    if to_currency == 'USD':
        for v in values:
            converted = round(v * rate, 2)
            formatted = format(converted, ',.2f')
            result.append('$' + formatted)
    else:
        for v in values:
            converted = round(v / rate, 2)
            formatted = format(converted, ',.2f')
            result.append(formatted + '€')
    return result
