import datetime

def elapsed_seconds(start, end):
    delta = end - start
    return int(delta.total_seconds())
