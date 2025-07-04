def mirror(text, sequence="abcdefghijklmnopqrstuvwxyz"):
    mirror_map = {}
    length = len(sequence)
    for i in range(length):
        mirror_map[sequence[i]] = sequence[length - 1 - i]
    
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in mirror_map:
            mirrored_char = mirror_map[lower_char]
            result.append(mirrored_char)
        else:
            result.append(char.lower())
    return ''.join(result)
