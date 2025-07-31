def doubles(s):
    changed = True

    while changed:
        changed = False
        i = 0
        new_s = ""
        n = len(s)

        while i < n:
            if i + 1 < n and s[i] == s[i + 1]:
                i += 2
                changed = True
            else:
                new_s += s[i]
                i += 1

        s = new_s
    return s
