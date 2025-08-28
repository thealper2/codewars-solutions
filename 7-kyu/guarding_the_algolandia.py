def find_needed_guards(k):
    n = len(k)
    count = 0
    i = 0
    while i < n - 1:
        if not k[i] and not k[i + 1]:
            count += 1
            k[i + 1] = True
            
        i += 1
        
    return count
