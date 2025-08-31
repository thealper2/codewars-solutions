def number_of_hooks(length,max_hook_dist):
    if length <= max_hook_dist:
        return 2
    
    hooks = 2
    while length / (hooks) > max_hook_dist:
        hooks *= 2
        
    return hooks + 1
