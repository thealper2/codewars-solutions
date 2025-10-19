def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'

    s = str(num)
    n = len(s)
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1]:
                return True
            
    return False
