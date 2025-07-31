def comes_after(st, l):
    result = ""
    st_lower = st.lower()
    l_lower = l.lower()

    for i in range(len(st) - 1):
        if st_lower[i] == l_lower and st[i + 1].isalpha():
            result += st[i + 1]

    return result
