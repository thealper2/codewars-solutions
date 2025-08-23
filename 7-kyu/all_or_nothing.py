def possibly_perfect(key, answers):
    correct_possible = True
    incorrect_possible = True
    
    for k, a in zip(key, answers):
        if k != '_':
            if k != a:
                correct_possible = False
            else:
                incorrect_possible = False
                
    return correct_possible or incorrect_possible
