def uncensor(infected, discovered):
    infected = list(infected)
    n = len(infected)
    idx = 0
    for c in discovered:
        for i in range(idx, n):
            if infected[i] == '*':
                infected[i] = c
                idx = i
                break
                
    return ''.join(infected)
