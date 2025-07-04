def change(st):
    result = ['0'] * 26
    for char in st:
        lower_char = char.lower()
        if 'a' <= lower_char <= 'z':
            index = ord(lower_char) - ord('a')
            result[index] = '1'
            
    return ''.join(result)
