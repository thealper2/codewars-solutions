def guess_my_number(guess, number = '123-451-2345'):
    result = ''
    for c in number:
        if c == '-':
            result += '-'
        elif c in guess:
            result += c
        else:
            result += '#'
            
    return result
