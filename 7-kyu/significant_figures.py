def number_of_sigfigs(num_str):
    if num_str.startswith(('+', '-')):
        num_str = num_str[1:]
    
    has_decimal = '.' in num_str
    
    if has_decimal:
        stripped = num_str.lstrip('0')
        if stripped.startswith('.'):
            stripped = '0' + stripped

        digits = stripped.replace('.', '')
        if int(digits) == 0:
            return 1
        
        return len(digits.lstrip('0'))
    else:
        stripped = num_str.lstrip('0')
        if not stripped:
            return 0
        
        stripped = stripped.rstrip('0')
        return len(stripped)
