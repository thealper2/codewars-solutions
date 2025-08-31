def who_is_online(friends):
    temp = {
        'online': [],
        'offline': [],
        'away': []
    }
    for friend in friends:
        if friend['status'] == 'offline':
            temp['offline'].append(friend['username'])
        elif friend['status'] == 'online' and friend['last_activity'] > 10:
            temp['away'].append(friend['username'])
        else:
            temp['online'].append(friend['username'])

    result = {}
    for k, v in temp.items():
        if v:
            result[k] = v
            
    return result
    
