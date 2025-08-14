def decipher(codes):
    idx = [[] for _ in range(len(codes[0]))]
    for code in codes:
        l = len(code)
        for i in range(l):
            idx[i].append(code[i])
            
    plaintext = ''
    for index in idx:
        if index:
            index_val = 0
            for c in index:
                index_val += ord(c) - ord('a') + 1 if c.isalpha() else 0

            index_val = index_val // len(index)
            if index_val == 0:
                plaintext += ' '
            else:
                plaintext += chr(index_val + ord('a') - 1) 
        
    return plaintext
