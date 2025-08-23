def test(r):
    avg = sum(r) / len(r)
    avg = round(avg, 3)
    d = {'h': 0, 'a': 0, 'l': 0}
    flag = False
    for c in r:
        if 9 <= c <= 10:
            d['h'] += 1
        elif 7 <= c <= 8:
            d['a'] += 1
        elif 1 <= c <= 6:
            d['l'] += 1
        else:
            flag = True

    result = [avg, d]
    if flag or (d['h'] > 0 and d['a'] == 0 and d['l'] == 0):
        result.append('They did well')

    return result
