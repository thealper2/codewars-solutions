from collections import OrderedDict


def first_non_repeated(s):
    count = OrderedDict()
    for c in s:
        count[c] = count.get(c, 0) + 1
        
    for c, cnt in count.items():
        if cnt == 1:
            return c
        
    return None
