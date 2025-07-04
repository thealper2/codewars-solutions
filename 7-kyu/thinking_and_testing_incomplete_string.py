def testit(s):
    n = len(s)
    result = ""
    
    for i in range(0, n, 2):
        if i + 1 < n:
            result += chr((ord(s[i]) + ord(s[i + 1])) // 2)
        else:
            result += chr((ord(s[i]) + ord(s[i])) // 2)
    return result
