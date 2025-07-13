import math

def gcd_matrix(a,b):
    m, n = len(a), len(b)
    average = 0
    
    for i in range(m):
        for j in range(n):
            average += math.gcd(a[i], b[j]) / (m * n)
            
    return round(average, 3)