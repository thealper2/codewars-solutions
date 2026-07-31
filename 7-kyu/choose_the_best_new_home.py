def choose_best_home(places, preferences, priorities):
    point_values = {trait: 6 - i for i, trait in enumerate(priorities[:6])}
    
    candidates = []
    for home_name, traits in places.items():
        score = 0
        for trait in priorities:
            if trait in point_values and trait in preferences and trait in traits:
                if traits[trait] == preferences[trait]:
                    score += point_values[trait]
                    
        candidates.append((home_name, score))
    
    candidates.sort(key=lambda x: (-x[1], x[0]))
    return candidates[0][0]
