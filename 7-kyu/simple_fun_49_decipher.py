def decipher(cipher):
    plaintext = ""
    i = 0
    n = len(cipher)

    while i < n:
        if int(cipher[i : i + 2]) < 97:
            plaintext += chr(int(cipher[i : i + 3]))
            i += 3
        else:
            plaintext += chr(int(cipher[i : i + 2]))
            i += 2

    return plaintext
