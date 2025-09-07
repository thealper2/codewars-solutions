from collections import defaultdict


def switch_dict(dic):
    d = defaultdict(list)
    for k, v in dic.items():
        d[v].append(k)
    
    return d
