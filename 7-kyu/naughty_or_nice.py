def what_list_am_i_on(actions):
    count = 0
    
    for action in actions:
        if action[0] in ['b', 'f', 'k']:
            count -= 1
        elif action[0] in ['g', 's', 'n']:
            count += 1
            
    return "nice" if count > 0 else "naughty"
