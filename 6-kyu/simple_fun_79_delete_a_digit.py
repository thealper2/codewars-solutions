def delete_digit(n):
    s = str(n)
    return max(map(int, [s[:i] + s[i+1:] for i in range(len(s))]))