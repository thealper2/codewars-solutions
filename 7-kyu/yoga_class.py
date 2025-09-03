def yoga(classroom, poses):
    total = 0
    
    for row in classroom:
        row_sum = sum(row)
        for pose in poses:
            for skill in row:
                if row_sum + skill >= pose:
                    total += 1
                    
    return total
