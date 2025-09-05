def london_city_hacker(journey): 
    tube_fare = 2.40
    bus_fare = 1.50
    total = 0.0
    bus_count = 0
    
    for leg in journey:
        if isinstance(leg, str):
            total += tube_fare
            if bus_count > 0:
                total += (bus_count + 1) // 2 * bus_fare
                bus_count = 0
        else:
            bus_count += 1
            
    if bus_count > 0:
        total += (bus_count + 1) // 2 * bus_fare
        
    return f"£{total:.2f}"
