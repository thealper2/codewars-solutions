def get_visible_name(filename):
    RTLO = "\u202E"
    real = filename[:filename.rindex('.')] if '.' in filename else filename
    if RTLO in real:
        i = real.index(RTLO)
        return real[:i] + real[i + 1:][::-1]
    
    return real
