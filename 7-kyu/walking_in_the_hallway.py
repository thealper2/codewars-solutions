def contact(hallway):
    n = len(hallway)
    min_steps = float('inf')
    for i in range(n):
        if hallway[i] == '>':
            for j in range(i + 1, n):
                if hallway[j] == '<':
                    steps = (j - i + 1) // 2
                    if steps < min_steps:
                        min_steps = steps
                        
    if min_steps != float('inf'):
        return min_steps
    
    return -1
