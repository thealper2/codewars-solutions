from re import sub, IGNORECASE

def filter_words(phrase):
    return sub(r"(bad|mean|ugly|horrible|hideous)", "awesome", phrase, flags=IGNORECASE)
