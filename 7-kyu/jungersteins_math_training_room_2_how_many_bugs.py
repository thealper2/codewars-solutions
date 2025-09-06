def cal_n_bug(n_head, n_leg, n_wing):
    total_heads = n_head
    total_legs = n_leg
    total_wings = n_wing
    
    if total_heads < 0 or total_legs < 0 or total_wings < 0:
        return [-1, -1, -1]
    
    temp = 8 * n_head - n_leg
    if temp < 0 or temp % 2 != 0:
        return [-1, -1, -1]
    
    b_plus_d = temp // 2
    d = total_wings - b_plus_d
    b = b_plus_d - d
    s = n_head - b_plus_d
    
    if s < 0 or b < 0 or d < 0:
        return [-1, -1, -1]
    
    if 8 * s + 6 * b + 6 * d != n_leg:
        return [-1, -1, -1]
    
    if b + 2 * d != n_wing:
        return [-1, -1, -1]
    
    return [s, b, d]
