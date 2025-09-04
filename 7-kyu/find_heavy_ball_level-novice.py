def find_ball(scales):
    left = [0, 1, 2]
    right = [3, 4, 5]
    w1 = scales.get_weight(left, right)
    if w1 < 0:
        w2 = scales.get_weight([0], [1])
        if w2 < 0:
            return 0
        elif w2 > 0:
            return 1
        else:
            return 2
        
    elif w1 > 0:
        w2 = scales.get_weight([3], [4])
        if w2 < 0:
            return 3
        elif w2 > 0:
            return 4
        else:
            return 5
        
    else:
        w2 = scales.get_weight([6], [7])
        if w2 < 0:
            return 6
        else:
            return 7
