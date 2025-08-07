def show_sequence(n):
    if n < 0:
        return f'{n}<0'
    
    if n == 0:
        return '0=0'
    
    nums = '+'.join(map(str, range(n + 1)))
    total = (n * (n + 1)) // 2
    return ' '.join([nums, '=', str(total)])
    
