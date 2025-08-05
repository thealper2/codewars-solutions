from collections import deque


def all_rationals():
    queue = deque()
    queue.append((1, 1))
    while queue:
        a, b = queue.popleft()
        yield (a, b)

        queue.append((a, a + b))
        queue.append((a + b, b))