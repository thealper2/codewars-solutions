def short_form(s):
    result = ""
    n = len(s)
    for i in range(n):
        if i == 0 or i == n - 1:
            result += s[i]
        elif s[i] not in "aeiouAEIOU":
            result += s[i]

    return result
