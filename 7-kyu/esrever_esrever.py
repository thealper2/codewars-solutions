def esrever(s):
    if not s:
        return s
    
    punctuation = s[-1] if s[-1] in {'.', '?', '!'} else ''
    text = s[:-1] if punctuation else s
    words = text.split()
    reversed_words = [word[::-1] for word in reversed(words)]
    result = ' '.join(reversed_words) + punctuation
    return result