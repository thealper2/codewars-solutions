def one_punch(s):
    if not isinstance(s, str):
        return 'Broken!'
    
    if not s:
        return 'Broken!'
    
    return ''.join([c for c in ' '.join(sorted(s.split())) if c.lower() not in {'e', 'a'}])

