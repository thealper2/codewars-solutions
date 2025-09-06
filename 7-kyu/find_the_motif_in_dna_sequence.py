def motif_locator(sequence, motif):
    l = len(motif)
    n = len(sequence)
    result = []
    for i in range(n - l + 1):
        if sequence[i:i+l] == motif:
            result.append(i + 1)
            
    return result
