def only_one(*args):
    found = False
    for arg in args:
        if arg and found:
            return False
        
        if arg:
            found = True
        
    return found
