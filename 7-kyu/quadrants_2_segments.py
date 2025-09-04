def quadrant_segment(A, B):
    def get_place(x, y):
        if x > 0 and y > 0:
            return 1
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
        elif x > 0 and y < 0:
            return 4
        
        return 5
    
    a_place = get_place(A.x, A.y)
    b_place = get_place(B.x, B.y)
    if a_place != b_place:
        return True
    else:
        return False
