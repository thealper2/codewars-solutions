def histogram(results):
    n = len(results)
    total = sum(results)
    result = []

    for i in range(n - 1, -1, -1):
        if results[i]:
            percentage = results[i] / total
            line = f"{i + 1}|{'#' * results[i]} {results[i]}"
            result.append(line)
        else:
            line = f"{i + 1}|"
            result.append(line)

    return "\n".join(result) + "\n"
