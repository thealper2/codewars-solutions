def square_color(file, rank):
    col_num = ord(file.lower()) - ord("a") + 1
    if (col_num + rank) % 2 == 0:
        return "black"
    else:
        return "white"
