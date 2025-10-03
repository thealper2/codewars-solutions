def find_hack(arr):
    hacked = []
    grade_points = {'A': 30, 'B': 20, 'C': 10, 'D': 5}
    for record in arr:
        name, reported_score, grades = record
        actual_score = 0
        all_b_or_above = True
        
        for grade in grades:
            actual_score += grade_points.get(grade, 0)
            if grade not in ['A', 'B']:
                all_b_or_above = False
                
        if len(grades) >= 5 and all_b_or_above:
            actual_score += 20
            
        actual_score = min(actual_score, 200)
        if actual_score != reported_score:
            hacked.append(name)
            
    return hacked
