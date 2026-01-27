def pick(preferred, blacklisted, options):
    valid_options = []
    for i, (skill, percentage) in enumerate(options):
        if skill in blacklisted:
            continue
            
        valid_options.append((i, skill, percentage))
        
    
    preferred_options = [(i, skill, percentage) for i, skill, percentage in valid_options if skill in preferred]
    if preferred_options:
        best = max(preferred_options, key=lambda x: x[2])
        return chr(ord('A') + best[0])
    
    neutral_options = [(i, skill, percentage) for i, skill, percentage in valid_options if skill not in preferred]
    if neutral_options:
        best = max(neutral_options, key=lambda x: x[2])
        return chr(ord('A') + best[0])
    
    return "D"
