def check_digit(number, index1, index2, digit):
    s = str(number)
    start = min(index1, index2)
    end = max(index1, index2) + 1
    sub = s[start:end]
    return str(digit) in sub
