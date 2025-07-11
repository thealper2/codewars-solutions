def contain_all_rots(strng, arr):
    n = len(strng)
    for i in range(n):
        rot = strng[i:] + strng[:i]
        if rot not in arr:
            return False
        
    return True
