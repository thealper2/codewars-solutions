def cycle(d, v, c):
    if c not in v:
        return None
    
    idx = v.index(c)
    new_idx = (idx + d) % len(v)
    return v[new_idx]