def potatoes(p0, w0, p1):
    dry_matter = w0 * (100 - p0)
    
    if dry_matter <= 0:
        return 0
    
    w1 = dry_matter / (100 - p1)
    return int(w1)
