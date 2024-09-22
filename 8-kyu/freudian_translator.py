def to_freud(sentence):
    return ' '.join(["sex" for _ in range(len(sentence.split(' ')))]) if len(sentence) > 0 else ""