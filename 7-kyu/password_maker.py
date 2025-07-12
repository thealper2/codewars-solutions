def make_password(phrase):
    letters = {'i': '1', 'o': '0', 's': '5'}
    return "".join(letters.get(word[0].lower(), word[0]) for word in phrase.split())