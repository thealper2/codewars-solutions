def no_musical(start_class, end_class, musical_performed_every, enrolment_duration):
    if musical_performed_every == 0:
        return end_class - start_class + 1
    
    if musical_performed_every <= enrolment_duration:
        return 0
    
    rem = (end_class - start_class) % musical_performed_every
    perfs = (end_class - start_class - rem) // musical_performed_every
    miss = musical_performed_every - enrolment_duration
    return perfs * miss + min(rem, miss)
