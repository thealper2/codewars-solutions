def autocomplete(input_, dictionary):
    search = ''.join(c for c in input_ if c.isalpha()).lower()
    
    return [
        word for word in dictionary
        if word.lower().startswith(search)
    ][:5]