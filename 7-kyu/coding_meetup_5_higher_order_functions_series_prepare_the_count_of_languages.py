def count_languages(lst): 
    lang = {}
    for d in lst:
        l = d['language']
        if l not in lang:
            lang[l] = 1
        else:
            lang[l] += 1
            
    return lang
