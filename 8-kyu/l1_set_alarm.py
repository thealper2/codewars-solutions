def set_alarm(employed, vacation):
    if employed == True:
        if vacation == True:
            return False
        else:
            return True
    else:
        return False
