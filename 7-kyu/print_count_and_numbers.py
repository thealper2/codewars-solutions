def count_me(data):
    if not data or not data.isdigit():
        return ""
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == current_char:
            i += 1
            count += 1
        result.append(f"{count}{current_char}")
        i += 1
    
    return "".join(result)
