def balanced_num(number):
    digits = []
    i = 0
    while 10 ** i < number:
        d = number // 10**i % 10
        digits.append(d)
        i += 1
        
    n = len(digits)
    mid = n // 2
    if n % 2 == 1:
        s1 = sum(digits[:mid])
        s2 = sum(digits[mid+1:])
    else:
        s1 = sum(digits[:mid-1])
        s2 = sum(digits[mid+1:])
    
    if s1 == s2:
        return 'Balanced'
    else:
        return 'Not Balanced'
