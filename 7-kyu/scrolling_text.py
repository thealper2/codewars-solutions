def scrolling_text(text):
    n = len(text)
    text = text.upper()
    result = []

    for i in range(n):
        result.append(text[i:] + text[:i])

    return result
