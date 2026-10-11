def str_to_hash(st): 
    result = {}
    if not st:
        return result
    
    params = st.split(', ')
    for param in params:
        param_name = param.split('=')[0]
        value = param.split('=')[1]
        result[param_name] = int(value)
        
    return result