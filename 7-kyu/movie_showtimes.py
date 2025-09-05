def movie_times(open_hour, close_hour, length):
    total_minutes_open = (close_hour - open_hour) * 60
    if total_minutes_open < 0:
        total_minutes_open += 24 * 60
        
    current_time = open_hour * 60
    results = []
    while current_time + length <= close_hour * 60 or (close_hour < open_hour and current_time + length <= close_hour * 60 + 24 * 60):
        hour = (current_time // 60) % 24
        minute = current_time % 60
        results.append((hour, minute))
        current_time += length + 15
        
    return results
