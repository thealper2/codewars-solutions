def freed_prisoners(prison):
    if not prison[0]:
        return 0
    
    count = 0
    i = 0
    while i < len(prison):
        if prison[i]:
            count += 1
            new_prison = []
            for j in range(i + 1, len(prison)):
                new_prison.append(not prison[j])
                
            prison = new_prison
            i = 0
        else:
            i += 1
            
    return count
