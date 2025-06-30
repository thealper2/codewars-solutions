def flip(d, a):
    if d == "L":
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
    else:
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

    return a
