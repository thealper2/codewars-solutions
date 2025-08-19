def diff(a, b):
    sa = set(a)
    sb = set(b)
    diff = []
    
    for i in sa:
        if i not in sb:
            diff.append(i)
        
    for i in sb:
        if i not in sa:
            diff.append(i)
            
    return sorted(diff)
