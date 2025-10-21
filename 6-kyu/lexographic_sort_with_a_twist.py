def custom_sort(lst):
    return sorted(lst, key=lambda s: [ord(c) for c in s] + [float('inf')])
