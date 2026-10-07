def get_winner(ballots):
    freq = {}
    max_vote = float('-inf')
    winner = None
    for ballot in ballots:
        freq[ballot] = freq.get(ballot, 0) + 1
        if freq[ballot] > max_vote:
            winner = ballot
            max_vote = freq[ballot]
            
    if len(freq) > 1 and all(v == max_vote for k, v in freq.items()):
        return None
    
    if max_vote <= len(ballots) / 2:
        return None
    
    return winner