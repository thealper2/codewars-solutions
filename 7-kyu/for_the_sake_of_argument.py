def numbers(*args):
    nums = list(args)
    for num in args:
        if type(num) not in [int, float]:
            return False
        
    return True
