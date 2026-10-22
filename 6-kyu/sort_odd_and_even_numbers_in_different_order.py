def sort_array(a):
    odds = sorted((x for x in a if x % 2 != 0))
    evens = sorted((x for x in a if x % 2 == 0), reverse=True)
    result = []
    oi = ei = 0
    for x in a:
        if x % 2 != 0:
            result.append(odds[oi])
            oi += 1
        else:
            result.append(evens[ei])
            ei += 1

    return result