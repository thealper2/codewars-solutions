def longest_slide_down(pyramid):
    best = list(pyramid[-1])
    for row in reversed(pyramid[:-1]):
        for i in range(len(row)):
            best[i] = row[i] + max(best[i], best[i + 1])
            
    return best[0]