def sum_of_integers_in_string(s):
    n = len(s)
    digits = []
    
    digit = ''
    for i in range(n):
        if s[i].isdigit():
            digit += s[i]
        else:
            if digit:
                digits.append(int(digit))
                
            digit = ''
            
    if digit:
        digits.append(int(digit))
        
    return sum(digits)