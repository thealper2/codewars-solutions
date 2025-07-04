def string_to_int_list(s):
    parts = s.split(',')
    integers = []
    for part in parts:
        if part.strip():
            integers.append(int(part))
            
    return integers
