def linked_sort(a_to_sort,a_linked,key=None):
    if key is None:
        key = lambda x: str(x)

    combined = sorted(zip(a_to_sort, a_linked), key=lambda x: key(x[0]))
    a_to_sort[:] = [x[0] for x in combined]
    a_linked[:] = [x[1] for x in combined]
    return a_to_sort
