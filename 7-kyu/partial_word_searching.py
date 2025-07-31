def word_search(query, seq):
    result = []
    for s in seq:
        if query.lower() in s.lower():
            result.append(s)

    if len(result) == 0:
        result.append("None")

    return result
