def segment_cover(A, L):
    if not A:
        return 0
    
    A.sort()
    segments = 1
    start = A[0]
    for point in A[1:]:
        if point > start + L:
            segments += 1
            start = point
    
    return segments
