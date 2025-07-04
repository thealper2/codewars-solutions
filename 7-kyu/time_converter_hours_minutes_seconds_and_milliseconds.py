def convert(time):
    hour = time.hour
    minute = time.minute
    second = time.second
    microsecond = time.microsecond
    millisecond = microsecond // 1000
    formatted_time = f"{hour:02d}:{minute:02d}:{second:02d},{millisecond:03d}"
    return formatted_time
