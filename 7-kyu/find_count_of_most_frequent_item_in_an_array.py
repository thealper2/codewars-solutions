def most_frequent_item_count(collection):
    if not collection:
        return 0

    count = {}
    max_val = float("-inf")

    for i in collection:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_val:
            max_val = count[i]

    return max_val
