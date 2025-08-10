def max_rot(n):
    s = str(n)
    max_num = n
    for i in range(len(s)):
        rotated = s[:i] + s[i+1:] + s[i]
        s = rotated
        current_num = int(rotated)
        if current_num > max_num:
            max_num = current_num
            
    return max_num