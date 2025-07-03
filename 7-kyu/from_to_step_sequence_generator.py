def generator (_from, _to, _step):
    if _step == 0:
        if _from > _to:
            return [x for x in range(_to, _from - 1, -1)]
        else:
            return [x for x in range(_from, _to + 1, -1)]
    else:
        if _from > _to:
            return [x for x in range(_from, _to - 1, -_step)]
        else:
            return [x for x in range(_from, _to + 1, _step)]
