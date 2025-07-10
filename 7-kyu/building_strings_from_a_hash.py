def solution(pairs):
    return ",".join([f"{k} = {v}" for k, v in pairs.items()])
