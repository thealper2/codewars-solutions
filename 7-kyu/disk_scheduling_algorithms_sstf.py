def sstf(requests, head):
    pending = list(requests)
    total = 0
    current = head
    while pending:
        best_idx = 0
        best_dist = abs(pending[0] - current)
        for i in range(1, len(pending)):
            d = abs(pending[i] - current)
            if d < best_dist:
                best_dist = d
                best_idx = i
        total += best_dist
        current = pending.pop(best_idx)
    return total