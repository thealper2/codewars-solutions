def alex_mistakes(number_of_katas, time_limit):
    kata_time = number_of_katas * 6
    remaining = time_limit - kata_time
    
    mistakes, pushup_time = 0, 5
    while remaining >= pushup_time:
        remaining -= pushup_time
        mistakes += 1
        pushup_time *= 2
        
    return mistakes
