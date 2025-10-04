def solution(*args):
    seen = set()
    args = list(args)
    for arg in args:
        if arg not in seen:
            seen.add(arg)
        else:
            return True
        
    return False
