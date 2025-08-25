def remove_duplicate_words(s):
    words = s.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
            
    return " ".join(result)
