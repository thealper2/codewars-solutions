def crossedwords(str1, str2):
    common_char = None
    pos_str1 = -1
    pos_str2 = -1
    for i, char in enumerate(str2):
        if char in str1:
            common_char = char
            pos_str2 = i
            pos_str1 = str1.index(char)
            break
    
    rows = len(str2)
    cols = len(str1)
    
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        grid[pos_str2][j] = str1[j]
    
    for i in range(rows):
        grid[i][pos_str1] = str2[i]
    
    result = []
    for row in grid:
        result.append(''.join(row))
    
    return '\n'.join(result) + '\n'
