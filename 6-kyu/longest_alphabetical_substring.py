def longest(s):
    if not s:
        return ''
    
    longest = current = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            current += s[i]
        else:
            current = s[i]
            
        if len(current) > len(longest):
            longest = current
            
    return longest
