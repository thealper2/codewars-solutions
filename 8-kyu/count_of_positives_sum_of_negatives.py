def count_positives_sum_negatives(arr):
    return (
        [len([_ for _ in arr if _ > 0]), sum([_ for _ in arr if _ < 0])]
        if len(arr) > 0
        else []
    )
