def oracle(gestures):
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    results = []
    for move in ['rock', 'paper', 'scissors']:
        score = 0
        for gesture in gestures:
            if move == gesture:
                score += 0
            elif wins[move] == gesture:
                score += 1
            else:
                score -= 1
                
        if score > 0:
            results.append(move)
            
    if not results:
        return 'tie'
    
    return '/'.join(results)
