def tricky_doubles(num):
    str_num = str(num)
    mid = len(str_num) // 2
    h1, h2 = str_num[:mid], str_num[mid:]
    return num * 2 if h1 != h2 else num
