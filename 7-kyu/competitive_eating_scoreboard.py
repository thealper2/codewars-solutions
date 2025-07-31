def scoreboard(who_ate_what):
    scores = []
    for c in who_ate_what:
        name = c["name"]
        score = (
            c.get("chickenwings", 0) * 5
            + c.get("hamburgers", 0) * 3
            + c.get("hotdogs", 0) * 2
        )
        scores.append({"name": name, "score": score})

    scores = sorted(scores, key=lambda x: x["name"])
    return sorted(scores, key=lambda x: x["score"], reverse=True)
