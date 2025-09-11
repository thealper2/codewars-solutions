def split_by_value(k, elements):
    less = [x for x in elements if x < k]
    greater_equal = [x for x in elements if x >= k]
    return less + greater_equal
