def get_grade(s1, s2, s3):
    avg_score = (s1 + s2 + s3) / 3
    if avg_score < 60:
        return "F"
    elif avg_score < 70:
        return "D"
    elif avg_score < 80:
        return "C"
    elif avg_score < 90:
        return "B"
    
    return "A"
