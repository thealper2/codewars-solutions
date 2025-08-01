def sort_by_value_and_index(arr):
    indexed_products = [(value * (i + 1), i, value) for i, value in enumerate(arr)]
    indexed_products.sort()
    sorted_arr = [value for (product, i, value) in indexed_products]
    return sorted_arr
