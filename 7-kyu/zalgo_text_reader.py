import unicodedata


def read_zalgo(zalgotext):
    normalized = unicodedata.normalize('NFD', zalgotext)
    return ''.join(c for c in normalized if unicodedata.category(c)[0] != 'M' and ord(c) < 128)
