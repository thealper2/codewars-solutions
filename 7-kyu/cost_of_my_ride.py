def insurance(age, size, num_of_days): 
    if num_of_days <= 0:
        return 0
    
    charge = 0 if age >= 25 else 10
    subcharge = 0
    if size == 'economy':
        subcharge = 0
    elif size == 'medium':
        subcharge = 10
    else:
        subcharge = 15
        
    return num_of_days * (50 + charge + subcharge)
