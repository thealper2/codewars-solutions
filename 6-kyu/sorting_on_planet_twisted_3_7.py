def sort_twisted37(arr):
    def twist(n):
        s = str(abs(n))
        swapped = ''.join('7' if c == '3' else '3' if c == '7' else c for c in s)
        return -int(swapped) if n < 0 else int(swapped)

    return sorted(arr, key=twist)