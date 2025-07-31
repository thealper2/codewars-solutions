from preloaded import alpha


def name_score(name):
    score = 0
    for char in name.upper():
        if char == " ":
            continue
        for letters, value in alpha.items():
            if char in letters:
                score += value
                break

    return {name: score}
