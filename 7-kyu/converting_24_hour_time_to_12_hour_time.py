def to_12_hour_time(time_str):
    hh = int(time_str[:2])
    mm = time_str[2:]
    period = 'am' if hh < 12 else 'pm'
    hour = hh % 12
    if hour == 0:
        hour = 12
        
    return f"{hour}:{mm} {period}"
