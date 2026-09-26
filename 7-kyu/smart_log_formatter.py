def smart_log_formatter(logs):
    if not logs:
        return []
    
    result = []
    n = len(logs)
    i = 0
    
    while i < n:
        j = 0
        while i + j < n and logs[i + j] == logs[i]:
            j += 1
        
        if j > 1:
            result.append(logs[i] + f" (x{j})")
        else:
            result.append(logs[i])
        
        i += j
    
    return result
