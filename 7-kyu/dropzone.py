import math


def dropzone(p, dropzones):
    n = len(dropzones)
    min_dist = float('inf')
    x1, y1 = p
    dropzone = None
    for i in range(n):
        x2, y2 = dropzones[i]
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if dist < min_dist:
            min_dist = dist
            dropzone = dropzones[i] 
        
    return dropzone
