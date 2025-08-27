def global_estimate(estimates):
    best = 0
    worst = 0
    avg = 0
    
    for low, high in estimates:
        best += low
        worst += high
        avg += (low + high) / 2
        
    return (best, avg, worst)
