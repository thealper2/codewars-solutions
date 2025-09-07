def remove_nth_element(lst, n):
    result = lst.copy()
    if n > len(result):
        return result
    
    return result[:n] + result[n + 1:]
    
