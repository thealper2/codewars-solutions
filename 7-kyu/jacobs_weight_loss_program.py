def lose_weight(gender, weight, duration):
    if gender not in ['F', 'M']:
        return "Invalid gender"
    
    if weight <= 0:
        return "Invalid weight"
    
    if duration <= 0:
        return "Invalid duration"
    
    lose = 0.015 if gender == 'M' else 0.012
    for _ in range(duration):
        loss = weight * lose
        weight -= loss
        
    return round(weight, 1)
