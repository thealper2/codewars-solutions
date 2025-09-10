def fist_beard(arr): 
    result = ''
    for item in arr:
        result += ''.join([chr(c) for c in item])
        
    return result
