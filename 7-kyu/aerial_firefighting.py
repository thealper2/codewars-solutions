def waterbombs(fire, w):
    sections = fire.split('Y')
    bombs = 0
    for section in sections:
        if section:
            bombs += (len(section) + w - 1) // w
            
    return bombs
