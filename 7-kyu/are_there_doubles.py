def double_check(strng):
    n = len(strng)
    strng = strng.lower()
    for i in range(n - 1):
        if strng[i:i+2] == strng[i:i+2][::-1]:
            return True
    
    return False
