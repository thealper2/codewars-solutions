def title_to_number(title):
    result = 0
    for c in title:
        result = result * 26 + ord(c) - ord('A') + 1
    return result