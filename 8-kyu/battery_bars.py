def battery_bars(percent):
    return "[" + "#" * (percent // 20) + "." * (5 - (percent // 20)) + "]"