def goto(level,button):
    valid_buttons = {'-3', '-2', '-1', '0', '1', '2', '3'}
    
    if not isinstance(level, int) or not isinstance(button, str):
        return 0
    
    if button not in valid_buttons:
        return 0
    
    if level < -3 or level > 3:
        return 0
    
    target_level = int(button)
    if target_level < -3 or target_level > 3:
        return 0
    
    return target_level - level if -3 <= target_level <= 3 else 0
