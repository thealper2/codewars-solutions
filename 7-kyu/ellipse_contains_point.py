def ellipse_contains_point(f0, f1, l, p): 
    d1 = ((p['x'] - f0['x'])**2 + (p['y'] - f0['y'])**2)**0.5
    d2 = ((p['x'] - f1['x'])**2 + (p['y'] - f1['y'])**2)**0.5
    return d1 + d2 <= l
