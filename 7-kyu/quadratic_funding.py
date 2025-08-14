def qf(donations: list, pool: int) -> list:
    sq = []
    for donation in donations:
        s_q = sum([d ** 0.5 for d in donation])
        sq.append((s_q ** 2) // 1)
    
    received = []
    for s in sq:
        r = pool * s / sum(sq)
        received.append(round(r))
    return received
