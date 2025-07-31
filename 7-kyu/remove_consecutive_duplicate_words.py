def remove_consecutive_duplicates(s: str) -> str:
    words = s.split()
    n = len(words)
    result = []

    for i in range(n):
        if i == 0:
            result.append(words[i])

        else:
            if words[i] != words[i - 1]:
                result.append(words[i])

    return " ".join(result)
