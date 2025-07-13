def make_backronym(acronym):
    return ' '.join(dictionary[letter.upper()] for letter in acronym)