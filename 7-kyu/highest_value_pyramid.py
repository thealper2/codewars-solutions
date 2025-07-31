from collections import defaultdict


def pyramid(stones):
    if not stones:
        return None

    count = defaultdict(int)
    for stone in stones:
        count[stone] += 1

    top_candidates = []
    middle_candidates = []
    bottom_candidates = []

    for num, cnt in count.items():
        if cnt >= 1:
            top_candidates.append(num)
        if cnt >= 2:
            middle_candidates.append(num)
        if cnt >= 3:
            bottom_candidates.append(num)

    max_sum = None

    for top in top_candidates:
        for middle in middle_candidates:
            if middle == top:
                continue
            for bottom in bottom_candidates:
                if bottom == top or bottom == middle:
                    continue
                current_sum = top + 2 * middle + 3 * bottom
                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum

    return max_sum
