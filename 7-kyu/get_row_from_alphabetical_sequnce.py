def get_row(N):
    N = (N - 1) % 26 + 1
    char = chr(ord("A") + N - 1)
    return char * N + "".join(chr(ord("A") + i) for i in range(N, 26))
