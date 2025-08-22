from datetime import datetime


def half_life(person1, person2):
    person1 = datetime.strptime(person1, "%Y-%m-%d").date()
    person2 = datetime.strptime(person2, "%Y-%m-%d").date()
    if person1 >= person2:
        diff = person1 - person2
        result = person1 + diff
    else:
        diff = person2 - person1
        result = person2 + diff
        
    return result.strftime('%Y-%m-%d')
