def what_time_is_it(angle):
    degrees = angle % 360
    total_seconds = degrees * 120
    hours, remainder = divmod(total_seconds, 3600)
    minutes = int(remainder // 60)

    if hours == 0:
        hours = 12

    hours = int(hours)
    return f'{hours:02d}:{minutes:02d}'