from collections import defaultdict


def find_the_missing_tree(trees):
    count = defaultdict(int)
    balance = float("-inf")
    for tree in trees:
        count[tree] += 1
        if count[tree] > balance:
            balance = count[tree]

    for k, v in count.items():
        if v != balance:
            return k

    return -1
