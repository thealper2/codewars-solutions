def check_three_and_two(arr):
    count_a = arr.count('a')
    count_b = arr.count('b')
    count_c = arr.count('c')
    
    if (count_a == 3 and count_b == 2) or (count_a == 2 and count_b == 3):
        return True
    if (count_a == 3 and count_c == 2) or (count_a == 2 and count_c == 3):
        return True
    if (count_b == 3 and count_c == 2) or (count_b == 2 and count_c == 3):
        return True
    return False
