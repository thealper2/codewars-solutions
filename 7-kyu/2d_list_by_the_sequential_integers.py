def make_2d_list(head, row, col):
    result = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(head)
            head += 1
            
        result.append(row)
        
    return result
