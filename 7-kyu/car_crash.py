def car_crash(road):
    lines = road.split('\n')
    for line in lines:
        car_index = line.find("O='`o")
        if car_index != -1:
            x_index = line.find('X', car_index)
            if x_index != -1:
                return True
            
    return False
