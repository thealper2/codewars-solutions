def sort_by_height(a):
    n = len(a)
    trees = [h for h in a if h != -1]
    trees.sort()
    people_index = 0

    for i in range(n):
        if a[i] != -1:
            a[i] = trees[people_index]
            people_index += 1

    return a
