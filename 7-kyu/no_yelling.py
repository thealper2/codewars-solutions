def filter_words(st):
    words = [word.strip() for word in st.split()]
    return words[0].capitalize() + ' ' + ' '.join([word.lower() for word in words[1:]])
