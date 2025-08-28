def pathfinder_scores(scores):
    cost_table = {
        7: -4,
        8: -2,
        9: -1,
        10: 0,
        11: 1,
        12: 2,
        13: 3,
        14: 5,
        15: 7,
        16: 10,
        17: 13,
        18: 17
    }
    
    total_cost = 0
    for score in scores:
        if score < 7 or score > 18:
            return False
        if score in cost_table:
            total_cost += cost_table[score]
        else:
            return False
    
    return total_cost <= 25
