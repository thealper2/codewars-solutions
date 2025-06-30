from collections import Counter


def pyramid(stones):
    d = Counter(stones)
    set_arr = sorted(list(set(stones)))

    if len(set_arr) < 3 or max(d.values()) < 3:
        return None

    arr3 = []
    arr2 = []
    arr1 = []

    for k, val in d.items():
        if val >= 3:
            arr3.append(k)
        elif val >= 2:
            arr2.append(k)
        else:
            arr1.append(k)

    result = 0
    for i in range(3, 0, -1):
        if i == 3:
            result += max(arr3) * 3
            arr3.remove(max(arr3))

        elif i == 2:
            result += max(arr2 + arr3) * 2
            if max(arr2 + arr3) in arr3:
                arr3.remove(max(arr2 + arr3))
            else:
                arr2.remove(max(arr2 + arr3))

        elif i == 1:
            result += max(arr1 + arr2 + arr3) * 1

    return result


stones = [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(pyramid(stones))
