def decipher_this(s):
    result = []
    for word in s.split():
        first_letter = ''
        remaining = []
        for ch in word:
            if ch.isdigit():
                first_letter += ch
            else:
                remaining.append(ch)

        first_letter = chr(int(first_letter))
        if len(remaining) > 1:
            remaining[0], remaining[-1] = remaining[-1], remaining[0]

        word = first_letter + ''.join(remaining)
        result.append(word)

    return ' '.join(result)