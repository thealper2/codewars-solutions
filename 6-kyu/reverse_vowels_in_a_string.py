def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    chars = list(s)
    positions = [i for i, c in enumerate(chars) if c in vowels]
    vowel_chars = [chars[i] for i in positions]
    for pos, v in zip(positions, reversed(vowel_chars)):
        chars[pos] = v

    return ''.join(chars)