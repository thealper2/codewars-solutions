def example_sort(arr, example_arr):
    return sorted(arr, key=lambda x: example_arr.index(x))
