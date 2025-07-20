def fire(x, y):
    matrix = [["top left",    "top middle",    "top right"],
              ["middle left", "center",        "middle right"],
              ["bottom left", "bottom middle", "bottom right"]]
    
    return matrix[y][x]