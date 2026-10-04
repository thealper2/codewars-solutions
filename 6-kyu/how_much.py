def howmuch(m, n):
    result = []

    for f in range(min(m, n), max(m, n) + 1):
        if (f - 1) % 9 == 0 and (f - 2) % 7 == 0:
            b = (f - 2) // 7
            c = (f - 1) // 9

            result.append([
                f"M: {f}",
                f"B: {b}",
                f"C: {c}"
            ])

    return result