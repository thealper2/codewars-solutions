def reverse_alternate(st):
    words = st.split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]

    return ' '.join(words)