def player_manager(players):
    if not players:
        return []
    
    result = []
    words = players.split(',')
    n = len(words)
    for i in range(0, n - 1, 2):
        result.append({
            'player': words[i].strip(),
            'contact': int(words[i + 1].strip())
        })
        
    return result
