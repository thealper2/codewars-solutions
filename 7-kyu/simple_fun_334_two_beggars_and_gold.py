def distribution_of(golds):
    A, B = 0, 0
    turn = True

    while golds:
        left, right = golds[0], golds[-1]
        
        if left >= right:
            taken = golds.pop(0)
        else:
            taken = golds.pop(-1)

        if turn:
            A += taken
        else:
            B += taken
            
        turn = not turn

    return [A, B]