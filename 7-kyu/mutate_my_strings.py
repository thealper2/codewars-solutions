def mutate_my_strings(s1, s2):
    if s1 == s2:
        return s1 + "\n"

    result = [s1]
    current = list(s1)
    target = list(s2)

    for i in range(len(current)):
        if current[i] != target[i]:
            current[i] = target[i]
            result.append("".join(current))

    return "\n".join(result) + "\n"
