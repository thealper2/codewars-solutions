def socks(colours, pairs):
    total = pairs * 2
    colours -= 1
    if colours > 0:
        total += colours
        
    return total