def watchtower(s: str) -> str:
    n = len(s)
    keep = [False] * n
    for i, ch in enumerate(s):
        if ch.isupper():
            keep[i] = True
            r = ord(ch) - ord('A') + 1
            for j in range(max(0, i - r), min(n, i + r + 1)):
                keep[j] = True
    return "".join(ch for i, ch in enumerate(s) if keep[i])