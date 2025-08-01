def tv_remote(word):
    keyboard = [
        ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
        ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
        ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
        ['p', 'q', 'r', 's', 't', '.', '@', '0'],
        ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']
    ]
    
    char_pos = {}
    n, m = len(keyboard), len(keyboard[0])
    
    for i in range(n):
        for j in range(m):
            char = keyboard[i][j]
            char_pos[char] = (i, j)
            
    current_pos = (0, 0)
    total = 0
    
    for c in word:
        target_pos = char_pos[c]
        row_diff = abs(target_pos[0] - current_pos[0])
        col_diff = abs(target_pos[1] - current_pos[1])
        total += row_diff + col_diff + 1
        current_pos = target_pos
        
    return total
