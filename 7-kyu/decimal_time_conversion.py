def to_industrial(time):
    if isinstance(time, str):
        hours, minutes = map(int, time.split(":"))
        total_minutes = hours * 60 + minutes
    else:
        total_minutes = time

    decimal_hours = round(total_minutes / 60, 2)
    return decimal_hours


def to_normal(time):
    total_minutes = round(time * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}:{minutes:02d}"
