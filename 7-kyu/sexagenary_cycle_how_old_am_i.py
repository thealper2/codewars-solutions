def how_old(birth, present):
    stems = "甲乙丙丁戊己庚辛壬癸"
    branches = "子丑寅卯辰巳午未申酉戌亥"
    cycle = [stems[i % 10] + branches[i % 12] for i in range(60)]
    b = cycle.index(birth)
    p = cycle.index(present)
    age = (p - b) % 60
    return 60 if age == 0 else age
