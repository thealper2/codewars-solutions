def unite_unique(*args):
    seen = set()
    result = []
    for arr in args:
        for item in arr:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result
