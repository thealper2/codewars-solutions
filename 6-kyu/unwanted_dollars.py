def money_value(s):
    try:
        return float(s.replace('$', '').replace(' ', '').strip())
    except ValueError:
        return 0.0