def describe_list(lst):
    if not lst:
        return 'empty'
    
    return 'singleton' if len(lst) == 1 else 'longer'