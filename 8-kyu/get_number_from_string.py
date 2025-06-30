def get_number_from_string(st):
    return int("".join([_ for _ in st if _.isdigit()]))
