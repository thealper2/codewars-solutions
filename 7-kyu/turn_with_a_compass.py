def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W' , 'NW']
    index = directions.index(facing)
    steps = turn // 45
    new_index = (index + steps) % 8
    return directions[new_index]
    
