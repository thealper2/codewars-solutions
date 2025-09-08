def can_play(hand, face_up):
    if not hand:
        return False
    
    face_color, face_num = face_up.split()
    for card in hand:
        color, num = card.split()
        if color == face_color or num == face_num:
            return True
        
    return False
