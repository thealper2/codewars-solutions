def find_warrior_rank(skill_points):
    if skill_points < 3:
        return "rathi"
    
    maha_count = skill_points // 10
    remaining = skill_points % 10
    
    ati_count = 0
    if remaining >= 8:
        maha_count += 1
    elif remaining >= 3:
        ati_count = 1
    
    parts = []
    for _ in range(maha_count):
        parts.append("maha")
    for _ in range(ati_count):
        parts.append("ati")
    parts.append("rathi")
    
    parts = sorted(parts, key=lambda x: ord(x[0]))
    return "-".join(parts)
