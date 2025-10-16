def ranks(a):
    s_a = sorted(set(a), reverse=True)
    rank_map = {}
    current_rank = 1
    for score in s_a:
        rank_map[score] = current_rank
        current_rank += a.count(score)
        
    return [rank_map[item] for item in a]
