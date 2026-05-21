def rumor_starter(record):
    all_people = set()
    for person, told_list in record.items():
        all_people.add(person)
        all_people.update(told_list)
        
    received = set()
    for told_list in record.values():
        received.update(told_list)
        
    starters = list(all_people - received)
    return sorted(starters)
