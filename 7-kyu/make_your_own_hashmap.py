def my_hash_map(list_of_strings):
    hash_dict = {}
    for s in list_of_strings:
        hash_val = sum(ord(c) for c in s)
        if hash_val not in hash_dict:
            hash_dict[hash_val] = []
            
        hash_dict[hash_val].append(s)
        
    return hash_dict
