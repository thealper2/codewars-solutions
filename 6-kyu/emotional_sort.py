def sort_emotions(arr, order):
    rank = {":D": 4, ":)": 3, ":|": 2, ":(": 1, "T_T": 0}
    return sorted(arr, key=lambda e: rank[e], reverse=order)