def convert_hash_to_array(dct):
    lst = []
    for k, v in dct.items():
        lst.append([k, v])
        
    lst = sorted(lst, key=lambda x: x[0])
    return lst
