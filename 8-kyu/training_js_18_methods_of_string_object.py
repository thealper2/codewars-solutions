def split_and_merge(string_, separator):
    return ' '.join([f'{separator}'.join(s) for s in string_.split()])