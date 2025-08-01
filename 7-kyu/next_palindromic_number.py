def next_pal(val):
    val += 1
    while True:
        str_val = str(val)
        if str_val == str_val[::-1]:
            return val
        
        val += 1
