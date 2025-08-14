def conjugate(verb):
    infinitive_suffix = verb[-2:]
    root = verb[:-2]
    conjugations = []
    
    if infinitive_suffix == 'ar':
        suffixes = ['o', 'as', 'a', 'amos', 'ais', 'an']
    elif infinitive_suffix == 'er':
        suffixes = ['o', 'es', 'e', 'emos', 'eis', 'en']
    elif infinitive_suffix == 'ir':
        suffixes = ['o', 'es', 'e', 'imos', 'is', 'en']
    else:
        return {verb: []}
    
    for suffix in suffixes:
        conjugations.append(root + suffix)
    
    return {verb: conjugations}
