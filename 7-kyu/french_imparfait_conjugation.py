def to_imparfait(verb_phrase):
    subject, infinitive_form = verb_phrase.split()
    d = {
        'Je': 'ais',
        'Tu': 'ais',
        'Il': 'ait',
        'Elle': 'ait',
        'On': 'ait',
        'Nous': 'ions',
        'Vous': 'iez',
        'Ils': 'aient',
        'Elles': 'aient'
    }
    return ' '.join([subject, infinitive_form[:-2] + d[subject]])
