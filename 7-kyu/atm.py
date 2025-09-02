def solve(n):
    count = 0
    
    while n >= 10:
        if n >= 500:
            n -= 500
        elif n >= 200:
            n -= 200
        elif n >= 100:
            n -= 100
        elif n >= 50:
            n -= 50
        elif n >= 20:
            n -= 20
        elif n >= 10:
            n -= 10
            
        count += 1
        
    return count if n == 0 else -1
