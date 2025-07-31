def shortest_time(n, m, speeds):
    if n == 1:
        return 0

    a, b, c, d = speeds
    elevator_time = (abs(m - n) * a) + b + c + ((n - 1) * a) + b
    walk_time = (n - 1) * d
    return min(elevator_time, walk_time)
