def meeting(s):
    people = s.upper().split(';')
    pairs = []
    for person in people:
        first, last = person.split(':')
        pairs.append((last, first))
        
    pairs.sort()
    return ''.join(f"({last}, {first})" for last, first in pairs)