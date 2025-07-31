def get_honor_path(honor_score, target_honor_score):
    required = target_honor_score - honor_score
    if required <= 0:
        return {}

    max_1kyus = required // 2
    remaining = required % 2

    if remaining == 0:
        return {"1kyus": max_1kyus, "2kyus": 0}
    else:
        if max_1kyus >= 0:
            return {"1kyus": max_1kyus, "2kyus": 1}
        else:
            return {"1kyus": 0, "2kyus": required}
