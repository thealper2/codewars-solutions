def replace_exclamation(st):
    return ''.join(["!" if letter in "aeiouAEIOU" else letter for letter in st])