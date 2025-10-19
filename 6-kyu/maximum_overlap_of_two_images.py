def max_overlap(img1, img2):
    n = len(img1)
    m = len(img1[0])
    max_overlap = 0
    
    for dx in range(-n + 1, n):
        for dy in range(-m + 1, m):
            overlap = 0
            for i in range(n):
                for j in range(m):
                    i2 = i + dx
                    j2 = j + dy
                    if 0 <= i2 < n and 0 <= j2 < m:
                        if img1[i][j] == 1 and img2[i2][j2] == 1:
                            overlap += 1
            max_overlap = max(max_overlap, overlap)
    
    return max_overlap
