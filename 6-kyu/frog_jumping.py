def solution(a):
    n = len(a)
    if n == 0:
        return 0

    pos = 0
    jumps = 0
    visited = set()
    while 0 <= pos < n:
        if pos in visited:
            return -1

        visited.add(pos)
        pos += a[pos]
        jumps += 1

    return jumps