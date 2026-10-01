import re

def increment_string(s):
    match = re.search(r'(\d+)$', s)
    if not match:
        return s + '1'

    num_str = match.group(1)
    prefix = s[:match.start()]
    new_num = str(int(num_str) + 1)

    if len(new_num) < len(num_str):
        new_num = new_num.zfill(len(num_str))

    return prefix + new_num