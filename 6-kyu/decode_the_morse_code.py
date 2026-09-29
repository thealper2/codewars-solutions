from preloaded import MORSE_CODE

def decode_morse(morse_code):
    return ' '.join(
        ''.join(MORSE_CODE[c] for c in word.split(' '))
        for word in morse_code.strip().split('   ')
    )