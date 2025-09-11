def is_matching(s, a, b): 
    s_clean = s.replace(" ", "").lower()
    combined = (a + b).replace(" ", "").lower()
    return sorted(s_clean) == sorted(combined)
