def enough(cap, on, wait):
    return on + wait - cap if on + wait - cap > 0 else 0
