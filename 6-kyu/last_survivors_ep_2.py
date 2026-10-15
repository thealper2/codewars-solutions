def last_survivors(s):
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1

    for i in range(26):
        carry = counts[i] // 2
        counts[i] %= 2
        if carry:
            nxt = (i + 1) % 26
            counts[nxt] += carry

    changed = True
    while changed:
        changed = False
        carry = counts[25] // 2
        if carry:
            counts[25] %= 2
            counts[0] += carry
            changed = True
        for i in range(25):
            carry = counts[i] // 2
            if carry:
                counts[i] %= 2
                counts[i + 1] += carry
                changed = True

    return ''.join(chr(ord('a') + i) * counts[i] for i in range(26))