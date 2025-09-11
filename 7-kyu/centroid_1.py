def centroid(c):
    n = len(c)
    x = sum(point[0] for point in c) / n
    y = sum(point[1] for point in c) / n
    z = sum(point[2] for point in c) / n
    return [round(x, 2), round(y, 2), round(z, 2)]
