import re

def rad_ladies(name):
    name = re.sub(r'[^a-zA-Z !]', '', name)
    return name.upper()