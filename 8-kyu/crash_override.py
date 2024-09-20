def alias_gen(f_name, l_name):
    f_key = f_name[0].upper()
    l_key = l_name[0].upper()

    if not f_key.isdigit() and not l_key.isdigit():
        return f"{FIRST_NAME[f_key]} {SURNAME[l_key]}"
    
    return 'Your name must start with a letter from A - Z.'