def build_a_wall(x=None,y=None):
    if not isinstance(x, int) or not isinstance(y, int) or x < 1 or y < 1:
        return None
    
    if x * y > 10000:
        return "Naah, too much...here's my resignation."
    
    rows = []
    for i in range(x):
        if (x - i) % 2 == 1:
            row = "■■|" * (y - 1) + "■■"
        else:
            row = "■|" + "■■|" * (y - 2) + "■■|■" if y > 1 else "■"
        rows.append(row)
    
    return '\n'.join(rows)
