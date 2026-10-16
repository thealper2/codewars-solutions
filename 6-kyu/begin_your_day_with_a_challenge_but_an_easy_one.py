def one_two_three(n):
    if n == 0:
        return [0, 0]
    
    q, r = divmod(n, 9)
    first = int('9' * q + (str(r) if r else ''))
    second = int('1' * n)
    return [first, second]