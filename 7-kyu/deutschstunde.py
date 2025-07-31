def der_die_das(wort):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'}
    for c in wort:
        if c.lower() in vowels:
            count += 1
            
    if count > 3:
        return "der " + wort
    elif count >= 2:
        return "die " + wort
    else:
        return "das " + wort
    
