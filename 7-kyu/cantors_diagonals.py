def cantor(nested_list):
    n = len(nested_list)
    return [1 - nested_list[i][i] for i in range(n)]
