def arr_adder(arr):
    m, n = len(arr), len(arr[0])
    result = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if arr[i][j] != "":
                result[j].append(arr[i][j])

    return " ".join(["".join(word) for word in result])
