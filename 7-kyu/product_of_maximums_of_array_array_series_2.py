def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    result = 1
    for item in lst[:n_largest_elements]:
        result *= item

    return result
