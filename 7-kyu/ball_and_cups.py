def cup_and_balls(b, arr):
    ball_position = b
    if not arr:
        return ball_position
    
    for switch in arr:
        cup1, cup2 = switch
        if ball_position == cup1:
            ball_position = cup2
        elif ball_position == cup2:
            ball_position = cup1
            
    return ball_position
