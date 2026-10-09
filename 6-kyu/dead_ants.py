def dead_ant_count(ants):
    return max(ants.count(c) for c in 'ant') - ants.count('ant')
