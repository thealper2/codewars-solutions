def is_same_language(lst):
    lang = lst[0]['language']
    for item in lst[1:]:
        if item['language'] != lang:
            return False
        
    return True
