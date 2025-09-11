def num_key_strokes(s):
    shift_chars = set('~!@#$%^&*()_+{}|:"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    strokes = 0
    for ch in s:
        if ch in shift_chars:
            strokes += 2
        else:
            strokes += 1
            
    return strokes
