def reverse_fun(s: str) -> str:
    n = len(s)
    for i in range(n):
        s = s[:i] + s[i:][::-1]

    return s
