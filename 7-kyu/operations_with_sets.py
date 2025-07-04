def process_2arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common = len(set1 & set2)
    unique = len(set1 ^ set2)
    remaining_arr1 = len(set1 - set2)
    remaining_arr2 = len(set2 - set1)
    return [common, unique, remaining_arr1, remaining_arr2]
