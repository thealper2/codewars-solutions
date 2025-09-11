def pass_or_fail(harmony):
    chords = [chord.split() for chord in harmony]
    for a, b in zip(chords, chords[1:]):
        if a != b:
            r = [pair for pair in zip(a, b) if len(set(pair)) >= 2]
            if len(set(tuple(x) for x in r)) < len(r):
                return 'Fail'
            
    return 'Pass'
