def new_numeral_system(number):
    result = []
    for i in range(ord(number) - ord('A') + 1):
        for j in range(i, ord(number) - ord('A') + 1):
            if i + j == ord(number) - ord('A'):
                text = chr(i + ord('A')) + " + " + chr(j + ord('A'))
                result.append(text)
                
    return result
