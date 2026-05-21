def wrapping_paper(boxes):
    total = 0
    for l, w, h in boxes:
        sides = [l * w, w * h, h * l]
        surface_area = 2 * sum(sides)
        slack = min(sides)
        total += surface_area + slack
        
    return total