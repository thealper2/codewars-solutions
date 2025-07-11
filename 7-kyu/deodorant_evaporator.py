def evaporator(content, evap_per_day, threshold):
    initial_content = content
    threshold_amount = (threshold / 100) * initial_content
    days = 0
    while content >= threshold_amount:
        content *= (100 - evap_per_day) / 100
        days += 1
        
    return days
