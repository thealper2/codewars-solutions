def what_is_the_time(time_in_mirror):
    hh, mm = map(int, time_in_mirror.split(':'))
    total = (hh % 12) * 60 + mm
    mirror = (720 - total) % 720
    mh, mmir = divmod(mirror, 60)
    if mh == 0:
        mh = 12
        
    return f'{mh:02d}:{mmir:02d}'