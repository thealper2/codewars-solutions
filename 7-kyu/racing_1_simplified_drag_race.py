def drag_race(length, anna, bob):
    anna_time = anna.reaction_time + length / anna.speed
    bob_time = bob.reaction_time + length / bob.speed
    
    if abs(anna_time - bob_time) < 1e-9:
        return "It's a draw"
    elif anna_time < bob_time:
        return "Anna is the winner"
    else:
        return "Bob is the winner"
