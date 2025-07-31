def negation_value(s, val):
    bool_val = bool(val)
    negations = len(s)
    if negations % 2 == 1:
        return not bool_val
    else:
        return bool_val
