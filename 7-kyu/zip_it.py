def lstzip(a,b,fn):
    la = len(a)
    lb = len(b)
    if la == lb:
        return [fn(a_, b_) for a_, b_ in zip(a, b)]
    elif la < lb:
        return [fn(a_, b_) for a_, b_ in zip(a, b[:la])]
    elif lb < la:
        return [fn(a_, b_) for a_, b_ in zip(a[:lb], b)]