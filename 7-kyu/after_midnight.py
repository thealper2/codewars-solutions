def day_and_time(mins):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    total_minutes = mins
    day_index = (total_minutes // (24 * 60)) % 7
    remaining_minutes = total_minutes % (24 * 60)
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60
    return f"{days[day_index]} {hours:02d}:{minutes:02d}"
