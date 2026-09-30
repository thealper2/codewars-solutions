def make_readable(seconds):
    minutes, remaining_seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    result = f"{hours:02}:{minutes:02}:{remaining_seconds:02}"
    return result