def get_middle(s):
    n = len(s)
    if n % 2 == 0:
        m = n // 2
        return s[m-1:m+1]
    else:
        return s[n // 2]
