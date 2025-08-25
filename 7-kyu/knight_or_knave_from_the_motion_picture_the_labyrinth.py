def knight_or_knave(said):
    if isinstance(said, bool):
        return 'Knight!' if said else 'Knave! Do not trust.'
    else:
        result = eval(said)
        return 'Knight!' if result else 'Knave! Do not trust.'
