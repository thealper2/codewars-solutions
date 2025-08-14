def solve(s):
    uppercase_count = 0
    lowercase_count = 0
    for c in s:
        if c.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
            
    if lowercase_count >= uppercase_count:
        return s.lower()
    else:
        return s.upper()
