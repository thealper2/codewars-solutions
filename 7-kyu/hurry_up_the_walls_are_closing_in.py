def can_escape(walls):
    for step, (left, right) in enumerate(walls):
        if left <= step + 1 or right <= step + 1:
            return False
        
    return True
