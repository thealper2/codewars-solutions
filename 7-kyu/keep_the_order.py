def keep_order(ary, val):
    for i, num in enumerate(ary):
        if num >= val:
            return i
        
    return len(ary)
