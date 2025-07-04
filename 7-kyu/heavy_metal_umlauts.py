def heavy_metal_umlauts(boring_text):
    umlaut_map = {
        'A': '\u00c4',
        'E': '\u00cb',
        'I': '\u00cf',
        'O': '\u00d6',
        'U': '\u00dc',
        'Y': '\u0178',
        'a': '\u00e4',
        'e': '\u00eb',
        'i': '\u00ef',
        'o': '\u00f6',
        'u': '\u00fc',
        'y': '\u00ff'
    }
    result = []
    for char in boring_text:
        if char in umlaut_map:
            result.append(umlaut_map[char])
        else:
            result.append(char)
    return ''.join(result)
