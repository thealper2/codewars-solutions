def sort_grades(grades):
    if not grades:
        return []
    
    grade_order = ['VB']
    for i in range(18):
        grade_order.append(f"V{i}")
        if i != 17:
            grade_order.append(f"V{i}+")

    sorted_grades = sorted(grades, key=lambda x: grade_order.index(x))
    return sorted_grades