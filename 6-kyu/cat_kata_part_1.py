import math

def peaceful_yard(yard, min_distance):
    cats = []
    for r, row in enumerate(yard):
        for c, ch in enumerate(row):
            if ch in 'LMR':
                cats.append((r, c))
                
    if len(cats) <= 1:
        return True
    
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            dr = cats[i][0] - cats[j][0]
            dc = cats[i][1] - cats[j][1]
            dist = math.sqrt(dr * dr + dc * dc)
            if dist < min_distance:
                return False
            
    return True