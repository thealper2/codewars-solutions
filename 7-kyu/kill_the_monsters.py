def kill_monsters(health, monsters, damage):
    hits = (monsters - 1) // 3
    total_damage = hits * damage
    remaining_health = health - total_damage
    if remaining_health <= 0:
        return "hero died"
    
    return f"hits: {hits}, damage: {total_damage}, health: {remaining_health}"
