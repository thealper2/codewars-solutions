from re import IGNORECASE, sub


def filter_words(phrase):
    return sub(r"(bad|mean|ugly|horrible|hideous)", "awesome", phrase, flags=IGNORECASE)
