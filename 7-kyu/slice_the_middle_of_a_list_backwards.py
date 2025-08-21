def reverse_middle(lst):
    n = len(lst)
    mid = (n + 1) // 2
    if n % 2 == 1:
        return [lst[mid], lst[mid - 1], lst[mid - 2]]
    else:
        return [lst[mid], lst[mid - 1]]
