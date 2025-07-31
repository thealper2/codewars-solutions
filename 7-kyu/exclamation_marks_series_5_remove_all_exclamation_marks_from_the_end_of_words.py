def remove(st):
    words = st.split()
    result = []
    for word in words:
        word = word.rstrip("!")
        result.append(word)

    return " ".join(result)
