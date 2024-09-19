def ensure_question(s):
    if len(s) > 0:
        return ''.join([s, '?']) if s[-1] != "?" else s
    else:
        return "?"
