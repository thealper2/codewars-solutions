def matryoshka(lists):
    if not lists:
        return True
    sorted_lists = sorted(lists, key=lambda x: min(x))
    for i in range(1, len(sorted_lists)):
        prev_min = min(sorted_lists[i-1])
        prev_max = max(sorted_lists[i-1])
        curr_min = min(sorted_lists[i])
        curr_max = max(sorted_lists[i])
        if curr_min <= prev_min or curr_max >= prev_max:
            return False
    return True
