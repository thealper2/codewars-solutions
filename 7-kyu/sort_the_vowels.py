def sort_vowels(s):
    if type(s) != str:
        return ''
    
    return '\n'.join(['|' + c if c in 'aeiouAEIOU' else c + '|' for c in s])