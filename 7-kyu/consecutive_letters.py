def solve(st):
    st = sorted(st.upper())
    n = len(st)
    for i in range(1, n):
        if ord(st[i]) - ord(st[i - 1]) != 1:
            return False
        
    return True
