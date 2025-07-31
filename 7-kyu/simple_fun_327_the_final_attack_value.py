import math


def final_attack_value(x, monster_list):
    current_attack = x
    for defense in monster_list:
        if defense <= current_attack:
            current_attack += defense
        else:
            current_attack += math.gcd(defense, current_attack)

    return current_attack
