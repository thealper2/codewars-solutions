def frame(phrase='', border='*'):
    if not phrase:
        return '****\n*  *\n*  *\n****'
    
    width = len(phrase) + 4
    top_bottom = border * width
    empty_line = border + " " * (width - 2) + border
    phrase_line = border + " " + phrase + " " + border
    return "\n".join([top_bottom, empty_line, phrase_line, empty_line, top_bottom])
