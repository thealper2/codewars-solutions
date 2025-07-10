def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    
    if name[2] in {'a', 'e', 'i', 'o', 'u'}:
        return name[:4].capitalize()
    else:
        return name[:3].capitalize()
