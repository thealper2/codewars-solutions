def right_depth(arr, constraints):
    if not constraints:
        return False

    depth_counts = {}

    for subarray in arr:
        current = subarray
        depth = 1
        while isinstance(current, list) and len(current) == 1:
            current = current[0]
            depth += 1
        if isinstance(current, list) and len(current) == 0:
            pass
        else:
            depth = 1

        if depth in depth_counts:
            depth_counts[depth] += 1
        else:
            depth_counts[depth] = 1

    for depth, count in depth_counts.items():
        if depth not in constraints:
            return False
        if count > constraints[depth]:
            return False

    return True
