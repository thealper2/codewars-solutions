def largest_sum(s):
    max_sum = float('-inf')
    temp = 0
    for c in s:
        if c == '0':
            max_sum = max(max_sum, temp)
            temp = 0
        else:
            temp += int(c)
            
    return max_sum
