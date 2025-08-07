def to_time(seconds):
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    return f'{hours} hour(s) and {minutes} minute(s)'
