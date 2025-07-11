def rounders(n):
    if n == 0:
        return 0
    
    while True:
        s = str(n)
        non_zero_pos = len(s) - 1
        while non_zero_pos >= 0 and s[non_zero_pos] == '0':
            non_zero_pos -= 1
        if non_zero_pos == 0:
            return n
        digit = int(s[non_zero_pos])
        power = 10 ** (len(s) - non_zero_pos - 1)
        if digit < 5:
            n = n - digit * power
        else:
            n = n + (10 - digit) * power
