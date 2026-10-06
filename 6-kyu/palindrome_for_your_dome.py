def palindrome(text):
    s = [c.lower() for c in text if c.isalpha() or c.isdigit()]
    n = len(s)
    mid = n // 2
    
    if n % 2 == 1:
        return s[:mid+1] == s[mid:][::-1]
    else:
        return s[:mid] == s[mid:][::-1]