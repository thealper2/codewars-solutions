def is_pangram(st):
    return len(set([c for c in st.lower() if c.isalpha()])) == 26