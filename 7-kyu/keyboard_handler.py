def handler(key, is_caps=False, is_shift=False):
    if not key or not isinstance(key, str) or len(key) != 1:
        return 'KeyError'
    
    if key.isupper() and not is_shift:
        return 'KeyError'
    
    if key.isalpha():
        if is_caps ^ is_shift:
            return key.upper()
        else:
            return key.lower()
    else:
        if is_shift:
            shift_map = {
                '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
                '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
                '-': '_', '=': '+', '[': '{', ']': '}', '\\': '|',
                ';': ':', "'": '"', ',': '<', '.': '>', '/': '?',
                '`': '~'
            }
            return shift_map.get(key, key)
        else:
            return key
