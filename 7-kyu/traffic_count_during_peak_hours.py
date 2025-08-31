def traffic_count(array):
    traffic = {
        '4:00pm': 0,
        '5:00pm': 0,
        '6:00pm': 0,
        '7:00pm': 0
    }
    
    n = len(array)
    for i in range(n):
        if i < 6:
            traffic['4:00pm'] = max(traffic['4:00pm'], array[i])
        elif i < 12:
            traffic['5:00pm'] = max(traffic['5:00pm'], array[i])
        elif i < 18:
            traffic['6:00pm'] = max(traffic['6:00pm'], array[i])
        elif i < 24:
            traffic['7:00pm'] = max(traffic['7:00pm'], array[i])
            
    return [(k, v) for k, v in traffic.items()]
