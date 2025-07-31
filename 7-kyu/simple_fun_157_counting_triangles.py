def counting_triangles(V):
    n = len(V)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a = V[i]
                b = V[j]
                c = V[k]
                if a + b > c and a + c > b and b + c > a:
                    count += 1

    return count
