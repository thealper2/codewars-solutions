def palindrome(num, s):
    if not isinstance(num, int) or not isinstance(s, int):
        return "Not valid"
    if isinstance(num, bool) or isinstance(s, bool) or num < 0 or s < 0:
        return "Not valid"
    
    result = []
    current = max(num, 10)
    while len(result) < s:
        if str(current) == str(current)[::-1]:
            result.append(current)
        current += 1
    
    return result