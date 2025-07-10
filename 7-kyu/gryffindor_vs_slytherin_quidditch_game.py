def game_winners(gryffindor, slytherin):
    gryffindor_point = gryffindor[0] + 150 if gryffindor[1] == 'yes' else gryffindor[0]
    slytherin_point = slytherin[0] + 150 if slytherin[1] == 'yes' else slytherin[0]
    
    if gryffindor_point > slytherin_point:
        return 'Gryffindor wins!'
    elif slytherin_point > gryffindor_point:
        return 'Slytherin wins!'
    else:
        return "It's a draw!"
