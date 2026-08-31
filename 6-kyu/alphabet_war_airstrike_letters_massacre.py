def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    
    chars = list(fight)
    
    killed = [False] * len(chars)
    
    for i, ch in enumerate(chars):
        if ch == '*':
            if i > 0 and chars[i-1] != '*':
                killed[i-1] = True
            if i + 1 < len(chars) and chars[i+1] != '*':
                killed[i+1] = True
    
    left_score = 0
    right_score = 0
    
    for i, ch in enumerate(chars):
        if ch == '*' or killed[i]:
            continue
        if ch in left_power:
            left_score += left_power[ch]
        elif ch in right_power:
            right_score += right_power[ch]
    
    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"