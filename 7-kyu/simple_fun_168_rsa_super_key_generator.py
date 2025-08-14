def super_key_generator(n):
    max_num = -1
    for five in range(0, n + 1, 3):
        three = n - five
        if three >= 0 and three % 5 == 0:
            candidate = '5' * five + '3' * three
            if candidate:
                candidate_num = int(candidate)
                if candidate_num > max_num:
                    max_num = candidate_num
    
    return str(max_num) if max_num != -1 else "-1"
