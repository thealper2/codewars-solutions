def twice_as_old(dad_years_old, son_years_old):
    if son_years_old == 0:
        return dad_years_old

    elif dad_years_old / son_years_old == 2:
        return 0

    return abs((dad_years_old - son_years_old) - son_years_old)
