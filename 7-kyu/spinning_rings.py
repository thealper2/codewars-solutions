def spinning_rings(inner_max, outer_max):
    inner, outer, moves = 0, 0, 0,
    while True:
        moves += 1
        inner = (inner - 1) % (inner_max + 1)
        outer = (outer + 1) % (outer_max + 1)
        if inner == outer:
            return moves
