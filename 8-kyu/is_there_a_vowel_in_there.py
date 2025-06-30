def is_vow(inp):
    d = {97: "a", 101: "e", 105: "i", 111: "o", 117: "u"}
    return [d[_] if _ in [97, 101, 105, 111, 117] else _ for _ in inp]
