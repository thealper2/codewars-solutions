def remove_char(array):
    result = []
    for item in array:
        new_item = '$'
        for c in item:
            if c.isdigit():
                new_item += c
        
        new_item = new_item[:-2] + "." + new_item[-2:]
        result.append(new_item)
        
    return result
