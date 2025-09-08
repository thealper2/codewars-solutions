def jumping(arr):
    hp = 20
    reduction_map = {'D': 0, 'B': 0.5, 'H': 0.8, 'W': 1}
    n = len(arr)
    for i in range(n - 1):
        current = arr[i].split()
        next_block = arr[i + 1].split()
        height_current = int(current[0])
        height_next = int(next_block[0])
        block_type = next_block[1]
        distance = height_current - height_next
        dmg_reduction = reduction_map[block_type]
        dmg = max(0, (distance - 3.5) * (1 - dmg_reduction))
        dmg = int(dmg)
        hp -= dmg
        if hp <= 0:
            return f'died on {i + 1}'
        
    return f'jumped to the end with {hp} remaining HP'
