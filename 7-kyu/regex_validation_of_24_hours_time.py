import re

def validate_time(time):
    pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    return bool(re.fullmatch(pattern, time))
