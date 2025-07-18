def switcher(arr):
    mapping = {
        1: 'z',
        2: 'y',
        3: 'x',
        4: 'w',
        5: 'v',
        6: 'u',
        7: 't',
        8: 's',
        9: 'r',
        10: 'q',
        11: 'p',
        12: 'o',
        13: 'n',
        14: 'm',
        15: 'l',
        16: 'k',
        17: 'j',
        18: 'i',
        19: 'h',
        20: 'g',
        21: 'f',
        22: 'e',
        23: 'd',
        24: 'c',
        25: 'b',
        26: 'a',
        27: '!',
        28: '?',
        29: ' '
    }
    result = []
    for num in arr:
        num_int = int(num)
        result.append(mapping[num_int])

    return ''.join(result)