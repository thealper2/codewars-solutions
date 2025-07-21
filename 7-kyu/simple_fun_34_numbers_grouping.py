def numbers_grouping(arr):
    group_counts = {}
    for num in arr:
        group = (num - 1) // 10**4 + 1
        if group in group_counts:
            group_counts[group] += 1
        else:
            group_counts[group] = 1
            
    total_lines = len(group_counts) + sum(group_counts.values())
    return total_lines