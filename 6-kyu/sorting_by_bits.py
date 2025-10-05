def sort_by_bit(arr): 
    arr.sort(key=lambda x: (x.bit_count(), x))
