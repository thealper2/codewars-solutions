def rank_of_element(arr, idx):
    n = len(arr)
    rank = 0

    for i in range(n):
        if i < idx and arr[i] <= arr[idx]:
            rank += 1
        elif i == idx:
            continue
        elif i > idx and arr[i] < arr[idx]:
            rank += 1

    return rank
