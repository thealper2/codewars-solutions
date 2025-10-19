def morse_converter(s):
    d = {
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
    }
    result = ''
    for i in range(0, len(s), 5):
        result += d.get(s[i:i+5])
        
    return int(result)
