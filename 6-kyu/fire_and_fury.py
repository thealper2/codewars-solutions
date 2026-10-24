import re

def fire_and_fury(tweet):
    if re.search(r'[^EFIRUY]', tweet):
        return "Fake tweet."
    
    matches = re.findall(r'FIRE|FURY', tweet)
    if not matches:
        return "Fake tweet."
    
    parts = []
    i = 0
    while i < len(matches):
        word = matches[i]
        count = 1
        while i + count < len(matches) and matches[i + count] == word:
            count += 1
            
        if word == 'FIRE':
            if count == 1:
                parts.append("You are fired!")
            else:
                parts.append("You " + "and you " * (count - 1) + "are fired!")
        else:
            if count == 1:
                parts.append("I am furious.")
            else:
                parts.append("I am " + "really " * (count - 1) + "furious.")
                
        i += count
        
    return ' '.join(parts)