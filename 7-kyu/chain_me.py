def chain(init_val, functions):
    for function in functions:
        init_val = function(init_val)
        
    return init_val
