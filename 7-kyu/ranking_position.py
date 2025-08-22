def ranking(people):
    if not people:
        return []
    
    sorted_people = sorted(people, key=lambda x: (-x['points'], x['name']))
    
    result = []
    position = 1
    prev_points = None
    for i, person in enumerate(sorted_people):
        if prev_points is None:
            person['position'] = position
        else:
            if person['points'] == prev_points:
                person['position'] = result[-1]['position']
            else:
                person['position'] = position
        result.append(person)
        prev_points = person['points']
        position += 1
    
    return result
