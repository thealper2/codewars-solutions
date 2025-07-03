def pluralize(word):
    if (
        word.endswith('s')
        or word.endswith('x')
        or word.endswith('z')
        or word.endswith('ch')
        or word.endswith('sh')
    ):
        return word + 'es'
    elif word.endswith('y') and word[-2] not in {'a', 'e', 'i', 'o', 'u'}:
        return word[:-1] + 'ies'
    else:
        return word + 's'
