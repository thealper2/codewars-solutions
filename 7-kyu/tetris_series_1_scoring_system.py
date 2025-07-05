def get_score(arr) -> int:
    n = len(arr)
    score = 0
    current_level = 0
    level = 0
    points = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}
    
    for i in range(n):
        current_level += arr[i]
        score += (level + 1) * points[arr[i]]
        if current_level >= 10:
            level += 1
            current_level = current_level % 10
            
    return score
    