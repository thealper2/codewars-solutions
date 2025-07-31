def find_function(func, arr):
    predicate = None
    for item in func:
        if callable(item):
            predicate = item
            break

    if not predicate:
        return []

    return [x for x in arr if predicate(x)]
