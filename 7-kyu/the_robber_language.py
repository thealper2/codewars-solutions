def robber_encode(sentence):
    vowels = "aeiouAEIOU"
    result = []
    for char in sentence:
        if char not in vowels and char.isalpha():
            o_char = "o" if char.islower() else "O"
            encoded = char + o_char + char
            result.append(encoded)
        else:
            result.append(char)
    return "".join(result)
