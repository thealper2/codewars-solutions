def elections_winners(votes, k):
    max_vote = max(votes)
    if k == 0:
        return 1 if votes.count(max_vote) == 1 else 0
    
    return sum(1 for v in votes if v + k > max_vote)
