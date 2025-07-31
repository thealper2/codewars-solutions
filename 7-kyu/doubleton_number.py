def doubleton(n):
    def is_doubleton(num):
        s = str(num)
        return len(set(s)) == 2
    
    current = n + 1
    while True:
        if is_doubleton(current):
            return current
        
        current += 1
