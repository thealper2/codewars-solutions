def rank(lst):
    indexed_elements = [(value, index) for index, value in enumerate(lst)]
    sorted_elements = sorted(indexed_elements, key=lambda x: x[0])
    ranks = [0.0] * len(lst)
    n = len(sorted_elements)
    i = 0
    while i < n:
        current_value = sorted_elements[i][0]
        start_index = i
        while i < n and sorted_elements[i][0] == current_value:
            i += 1
        end_index = i - 1
        average_rank = (start_index + end_index) / 2.0
        for j in range(start_index, end_index + 1):
            original_index = sorted_elements[j][1]
            ranks[original_index] = average_rank
    return ranks
