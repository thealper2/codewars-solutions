def is_alt(s):
    vowels = "aeiou"

    for i in range(len(s) - 1):
        if (s[i] in vowels) == (s[i + 1] in vowels):
            return False

    return True