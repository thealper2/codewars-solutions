def next_item(xs, item):
    if hasattr(xs, '__getitem__'):
        n = len(xs)
        for i in range(n):
            if xs[i] == item and i < n - 1:
                return xs[i + 1]
        return None
    
    found = False
    for current in xs:
        if found:
            return current
        if current == item:
            found = True
    
    return None