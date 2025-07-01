def scoreboard(st):
    words = st.split()
    scores = {
        'nil': 0,
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    result = []
    for word in words:
        if word.lower() in scores.keys():
            result.append(scores[word.lower()])

    return result