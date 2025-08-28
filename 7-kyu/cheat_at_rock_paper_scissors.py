import random


def r_p_s_cheat(choice):
    if random.random() < 0.9:
        if choice == 'rock':
            return 'paper'
        elif choice == 'paper':
            return 'scissors'
        else:
            return 'rock'
        
    else:
        if choice == 'rock':
            return 'scissors'
        elif choice == 'paper':
            return 'rock'
        else:
            return 'paper'
