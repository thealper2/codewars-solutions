def chore_assignment(chores):
    chores_sorted = sorted(chores)
    workloads = []
    left = 0
    right = len(chores_sorted) - 1

    while left <= right:
        if left == right:
            workloads.append(chores_sorted[left])
        else:
            workloads.append(chores_sorted[left] + chores_sorted[right])
        left += 1
        right -= 1

    return sorted(workloads)
