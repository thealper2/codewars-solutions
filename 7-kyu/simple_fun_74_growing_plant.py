def growing_plant(up_speed, down_speed, desired_height):
    height = 0
    count = 0
    if up_speed - down_speed >= desired_height:
        return 1
    
    while height < desired_height:
        height += up_speed
        count += 1
        
        if height >= desired_height:
            return count
        
        
        height -= down_speed
        
    return count