def parse_int(string):
    words = string.replace('-', ' ').replace(' and ', ' ').split()
    units = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    }
    tens = {
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    }

    total = 0
    current = 0
    for w in words:
        if w in units:
            current += units[w]
        elif w in tens:
            current += tens[w]
        elif w == 'hundred':
            current *= 100
        elif w == 'thousand':
            total += current * 1000
            current = 0
        elif w == 'million':
            total += current * 1000000
            current = 0
    total += current
    return total