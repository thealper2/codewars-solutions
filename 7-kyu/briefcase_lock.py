def min_turns(current, target):
    total = 0
    for c, t in zip(current, target):
        c = int(c)
        t = int(t)
        forward = abs(c - t)
        backward = 10 - forward
        total += min(forward, backward)
        
    return total
