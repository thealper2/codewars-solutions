import re


def moment_of_time_in_space(moment):
    time_chars = re.findall(r'[1-9]', moment)
    space = len(moment) - len(time_chars)
    time = sum(int(c) for c in time_chars)
    
    result = [False, False, False]
    result[1 + (1 if time > space else -1 if time < space else 0)] = True
    return result
