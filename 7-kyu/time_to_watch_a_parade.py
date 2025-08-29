def parade_time(groups, location, speed, pref):
    result = []
    for i, c in enumerate(groups, start=1):
        if c == pref:
            result.append((location + i) // speed)
            
    return result
