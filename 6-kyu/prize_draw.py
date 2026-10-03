def rank(st, we, n):
    if not st:
        return "No participants"

    names = st.split(',')
    if n > len(names):
        return "Not enough participants"
    
    scores = []
    for w, name in zip(we, names):
        score = (len(name) + sum(ord(c.lower()) - ord('a') + 1 for c in name)) * w
        scores.append((name, score))
        
    scores.sort(key=lambda x: (-x[1], x[0]))
    return scores[n - 1][0]