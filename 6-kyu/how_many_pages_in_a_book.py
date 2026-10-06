def amount_of_pages(summary):
    if summary <= 0:
        return 0
    
    digits = summary
    pages = 0
    d = 1
    count = 9
    
    while digits > d * count:
        digits -= d * count
        pages += count
        d += 1
        count *= 10
        
    pages += digits // d
    return pages