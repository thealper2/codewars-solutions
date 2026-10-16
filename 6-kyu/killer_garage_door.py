def controller(events):
    position = 0
    direction = 0
    motion = 0
    result = []
    
    for e in events:
        if e == 'P':
            if direction != 0:
                motion = direction
                direction = 0
            else:
                if motion != 0 and 0 < position < 5:
                    direction = motion
                elif position == 0:
                    direction = 1
                    motion = 1
                elif position == 5:
                    direction = -1
                    motion = -1
        elif e == 'O':
            if direction == 1 or motion == 1:
                direction = -1
                motion = -1
            elif direction == -1 or motion == -1:
                direction = 1
                motion = 1
        
        if direction != 0:
            position += direction
        if position >= 5:
            position = 5
            direction = 0
            motion = 0
        elif position <= 0:
            position = 0
            direction = 0
            motion = 0
        
        result.append(str(position))
    
    return ''.join(result)