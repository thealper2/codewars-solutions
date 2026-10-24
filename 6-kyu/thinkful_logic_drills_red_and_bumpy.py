def color_probability(color, texture):
    smooth = {'red': 1, 'yellow': 1, 'green': 1}
    bumpy = {'red': 4, 'yellow': 2, 'green': 1}
    
    if texture == 'smooth':
        counts = smooth
    else:
        counts = bumpy
        
    total = sum(counts.values())
    prob = counts[color] / total
    
    return f"{int(prob * 100) / 100:.2f}"