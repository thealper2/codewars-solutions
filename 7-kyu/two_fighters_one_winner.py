def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        attacker, defender = fighter1, fighter2
    else:
        attacker, defender = fighter2, fighter1

    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name

        attacker, defender = defender, attacker
