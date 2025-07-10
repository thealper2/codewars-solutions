def is_planet_mnemonic_correct(solar_system, mnemonic):
    mnemonic_words = mnemonic.split()
    mnemonic_index = 0
    
    for planet in solar_system:
        if planet == "Asteroid":
            continue

        if mnemonic_index >= len(mnemonic_words):
            return False

        planet_first_char = planet[0].upper()
        word_first_char = mnemonic_words[mnemonic_index][0].upper()
        if planet_first_char != word_first_char:
            return False
        
        mnemonic_index += 1

    return mnemonic_index == len(mnemonic_words)
