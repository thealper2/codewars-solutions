def kata_13_december(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = "_"

    return [_ for _ in lst if _ != "_"]
