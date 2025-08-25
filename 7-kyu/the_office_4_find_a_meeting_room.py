def meeting(rooms):
    n = len(rooms)
    for i in range(n):
        if rooms[i] == 'O':
            return i
        
    return 'None available!'
