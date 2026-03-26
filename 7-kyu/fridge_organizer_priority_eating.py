def fridge_organizer(items):
    not_expired = [item for item in items if item.expiry_days >= 0]
    
    result = sorted(not_expired, key=lambda x: (
        not x.is_almost_empty,
        x.expiry_days,
        x.name,
    ))
    
    return [item.name for item in result]
