def reverse_message(text):
    return ' '.join([word.capitalize() for word in text[::-1].split()]) if text else ''
