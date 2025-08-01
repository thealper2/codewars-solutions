def kooka_counter(laughing):
    count = 0
    n = len(laughing)
    prev = None
    for i in range(0, n, 2):
        if laughing[i:i+2] == 'ha' and prev != 'ha':
            count += 1
        elif laughing[i:i+2] == 'Ha' and prev != 'Ha':
            count += 1
            
        prev = laughing[i:i+2]
        
    return count
