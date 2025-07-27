def shuffled_array(s):
    total_sum = sum(s)
    original_sum = total_sum // 2
    temp = list(s)
    temp.remove(original_sum)
    temp.sort()
    return temp