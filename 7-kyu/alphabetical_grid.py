def grid(N):
    if N < 0:
        return None

    result = []
    for i in range(N):
        row = [(chr((ord('a') + i + j - ord('a')) % 26 + ord('a'))) for j in range(N)]
        result.append(" ".join(row))

    return "\n".join(result)
