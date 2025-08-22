def koch_curve(n):
    if n == 0:
        return []
    
    angles = []
    def generate(n):
        if n == 0:
            return
        generate(n-1)
        angles.append(60)
        generate(n-1)
        angles.append(-120)
        generate(n-1)
        angles.append(60)
        generate(n-1)
    
    generate(n)
    return angles
