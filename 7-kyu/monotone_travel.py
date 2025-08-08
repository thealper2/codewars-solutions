def is_monotone(heights):
    n = len(heights)
    for i in range(1, n):
        if heights[i] < heights[i - 1]:
            return False
        
    return True
