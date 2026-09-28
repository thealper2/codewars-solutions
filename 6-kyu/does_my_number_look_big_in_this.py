def narcissistic( value ):
    s = str(value)
    n = len(s)
    result = sum(int(c) ** n for c in s)
    return result == value