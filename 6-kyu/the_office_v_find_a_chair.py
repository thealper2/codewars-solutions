def meeting(rooms, need):
    if need == 0:
        return 'Game On'

    result = []
    for occupants, chairs in rooms:
        taken = len(occupants)
        spare = max(0, chairs - taken)
        if spare >= need:
            result.append(need)
            return result

        result.append(spare)
        need -= spare

    return 'Not enough!'