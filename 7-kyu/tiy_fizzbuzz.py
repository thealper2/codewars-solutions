def tiy_fizz_buzz(string):
    lower_vowels = "aeiou"
    upper_vowels = "AEIOU"
    result = ""
    for c in string:
        if c in lower_vowels:
            result += "Yard"
        elif c in upper_vowels:
            result += "Iron Yard"
        elif c.isupper() and c not in upper_vowels:
            result += "Iron"
        elif c.islower() and c not in lower_vowels:
            result += c
        else:
            result += c

    return result
