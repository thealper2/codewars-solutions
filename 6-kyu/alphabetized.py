def alphabetized(s):
    return ''.join(sorted(''.join(c for c in s if c.isalpha()), key=str.lower))