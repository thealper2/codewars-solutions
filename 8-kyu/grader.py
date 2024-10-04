def grader(score):
    if score > 1.0:
        return "F"
    else:
        if score < 0.6:
            return "F"
        elif score < 0.7:
            return "D"
        elif score < 0.8:
            return "C"
        elif score < 0.9:
            return "B"
        else:
            return "A"
