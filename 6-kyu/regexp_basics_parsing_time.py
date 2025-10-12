import re


def to_seconds(time_str):
    pattern = r'^(\d{2}):([0-5]\d):([0-5]\d)$'
    m = re.match(pattern, time_str.strip())
    
    if m and len(time_str) == 8:
        hours, minutes, seconds = m.groups()
        hours_int = int(hours)
        if hours_int <= 99:
            return hours_int * 3600 + int(minutes) * 60 + int(seconds)
    
    return None
