import re


def is_a_valid_message(message):
    if message == "":
        return True

    tokens = re.findall(r'\d+|[A-Za-z]+', message)
    
    if not tokens or not tokens[0].isdigit():
        return False
    if len(tokens) % 2 != 0:
        return False
    
    for i in range(0, len(tokens), 2):
        num = tokens[i]
        word = tokens[i + 1]
        if not word.isalpha():
            return False
        if int(num) != len(word):
            return False
    
    return True