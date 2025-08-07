def name_value(my_list):
    result = []
    for index, s in enumerate(my_list, start=1):
        value = 0
        for char in s:
            if char != ' ':
                value += ord(char.lower()) - ord('a') + 1
        result.append(value * index)
        
    return result
