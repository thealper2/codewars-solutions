def fantastic_person(table):
    n = len(table)
    for i in range(n):
        if all(table[i][j] for j in range(n)) and all(not table[j][i] for j in range(n) if j != i):
            return i
        
    return -1
