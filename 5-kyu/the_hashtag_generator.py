def generate_hashtag(s):
    if not s or not s.strip():
        return False
    
    words = s.split()
    result = '#' + ''.join(w.capitalize() for w in words)
    return result if len(result) <= 140 else False