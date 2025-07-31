def sort_by_language(arr):
    arr = sorted(arr, key=lambda x: x["first_name"])
    return sorted(arr, key=lambda x: x["language"])
