def solve(s):
    vowels = 'aeiou'
    max_len = curr_len = 0

    for char in s:
        if char in vowels:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0

    return max_len
