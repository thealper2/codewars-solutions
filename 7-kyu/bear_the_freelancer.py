def bear_dollars(jobs):
    if not jobs:
        return 0
    
    rate_map = {
        'close friend': 25,
        'friend': 50,
        'acquaintance': 100
    }
    
    total = 0
    for hours, client_type in jobs:
        lower_client = client_type.lower()
        rate = rate_map.get(lower_client, 125)
        total += hours * rate
    
    return total
