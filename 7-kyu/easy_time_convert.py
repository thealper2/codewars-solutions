def time_convert(num):
    if num <= 0:
        return "00:00"
    
    hours = str(num // 60)
    minutes = str(num - int(hours) * 60)
    return f"{hours.zfill(2)}:{minutes.zfill(2)}"
