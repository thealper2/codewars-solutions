import re


def gym_slang(s):
    def replace_match(match):
        word = match.group(0)
        lower_word = word.lower()
        if lower_word == "probably":
            return "prolly" if word.islower() else "Prolly"
        elif lower_word == "i am":
            return "i'm" if word.islower() else "I'm"
        elif lower_word == "instagram":
            return "insta" if word.islower() else "Insta"
        elif lower_word == "do not":
            return "don't" if word.islower() else "Don't"
        elif lower_word == "going to":
            return "gonna" if word.islower() else "Gonna"
        elif lower_word == "combination":
            return "combo" if word.islower() else "Combo"
        return word

    patterns = [
        r'probably', r'i am', r'instagram', r'do not', r'going to', r'combination'
    ]
    
    for pattern in patterns:
        s = re.sub(pattern, replace_match, s, flags=re.IGNORECASE)
    
    return s
