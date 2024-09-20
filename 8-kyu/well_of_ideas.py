def well(x):
    count = 0
    for a in x:
        if a == "good":
            count += 1
            
    if count == 0:
        return "Fail!"
    
    elif count <= 2:
        return "Publish!"
    
    else:
        return "I smell a series!"