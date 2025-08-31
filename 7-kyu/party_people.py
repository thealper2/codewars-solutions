def party_people(lst):
    changed = True
    while changed:
        changed = False
        n = len(lst)
        new_lst = [x for x in lst if x <= n]
        if len(new_lst) != n:
            changed = True
            lst = new_lst
            
    return len(lst)
