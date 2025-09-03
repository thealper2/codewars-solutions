def total_amount_visible(top_num, num_of_sides):
    total_sum = num_of_sides * (num_of_sides + 1) // 2
    bottom_num = num_of_sides + 1 - top_num
    return total_sum - bottom_num
