def dots_on_domino_bones(n):
    total = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            total += i + j
            
    return total
