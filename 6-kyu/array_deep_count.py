def deep_count(a):
    cnt = 0
    for item in a:
        cnt += 1
        if isinstance(item, list):
            cnt += deep_count(item)

    return cnt
