def rotate(data, n):
    if not data:
        return data
    
    k = n % len(data)
    return data[-k:] + data[:-k] if k else data[:]