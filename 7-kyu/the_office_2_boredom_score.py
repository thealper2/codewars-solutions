def boredom(staff):
    department_scores = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }

    total_score = 0
    for department in staff.values():
        total_score += department_scores.get(department, 0)

    if total_score <= 80:
        return "kill me now"
    elif total_score < 100:
        return "i can handle this"
    else:
        return "party time!!"
