def house_of_cats(legs):
    max_people = legs // 2
    result = []
    for people in range(max_people + 1):
        remaining_legs = legs - people * 2
        if remaining_legs >= 0 and remaining_legs % 4 == 0:
            result.append(people)
    return result
