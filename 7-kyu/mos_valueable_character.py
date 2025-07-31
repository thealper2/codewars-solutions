def solve(s):
    first_occurrence = {}
    last_occurrence = {}
    
    for index, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = index
        last_occurrence[char] = index
    
    max_value = -1
    result_char = None
    
    for char in first_occurrence:
        value = last_occurrence[char] - first_occurrence[char]
        if value > max_value:
            max_value = value
            result_char = char
        elif value == max_value:
            if char < result_char:
                result_char = char
    
    return result_char
