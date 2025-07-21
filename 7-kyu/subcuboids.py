def subcuboids(x,y,z):
    sum_x = x * (x + 1) // 2
    sum_y = y * (y + 1) // 2
    sum_z = z * (z + 1) // 2
    return sum_x * sum_y * sum_z