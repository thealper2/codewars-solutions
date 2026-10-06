def calculate_damage(your_type, opponent_type, attack, defense):
    d = {
        'fire': { 'electric': 1.0, 'fire': 0.5, 'grass': 2.0, 'water': 0.5 },
        'grass': { 'electric': 1.0, 'fire': 0.5, 'grass': 0.5, 'water': 2.0 },
        'water': { 'electric': 0.5, 'fire': 2.0, 'grass': 0.5, 'water': 0.5 },
        'electric': { 'electric': 0.5, 'fire': 1.0, 'grass': 1.0, 'water': 2.0 },
    }
    damage = 50 * (attack / defense) * d[your_type][opponent_type]
    return damage