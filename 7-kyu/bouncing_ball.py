def bouncing_ball(initial, proportion):
    bounces = 0
    height = initial
    while height > 1:
        height *= proportion
        bounces += 1
    
    return bounces
