def find_missing_numbers(arr):
    return [i for i in range(min(arr), max(arr)) if i not in arr] if arr else []