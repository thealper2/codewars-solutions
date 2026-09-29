def count(s):
    return {c: s.count(c) for c in set(s)}