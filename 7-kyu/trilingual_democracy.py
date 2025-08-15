def trilingual_democracy(group):
    set_group = set(group)
    if len(set_group) == 1:
        return group[0]
    
    elif len(set_group) == 2:
        min_val = float('inf')
        min_key = None
        for item in list(set_group):
            d = group.count(item)
            if d < min_val:
                min_val = d
                min_key = item
                
        return min_key
    
    elif len(set_group) == 3:
        seen = set()
        langs = ['D', 'F', 'I', 'K']
        for item in list(set_group):
            if item not in seen:
                langs.remove(item)
                seen.add(item)
                
        return langs[0]
