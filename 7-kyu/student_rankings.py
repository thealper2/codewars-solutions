def post_grades(students):
    if not students:
        return []
    
    result = []
    for student in students:
        id, _, grades = student.split('-')
        count = 0
        sum_grades = 0
        for grade in grades.split():
            if grade != '':
                grade = grade.strip()
                grade = float(grade)
                sum_grades += grade
                count += 1
            
        result.append((id.strip(), sum_grades / count))
        
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result
