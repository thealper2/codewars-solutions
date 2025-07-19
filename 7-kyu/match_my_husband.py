def match(usefulness, months):
    useful = sum(usefulness)
    remain = 100.
    for _ in range(months):
        remain -= (remain * 0.15)
        
    if useful >= remain:
        return "Match!"
    else:
        return "No match!"