def jumbler(indices):
    nums = list(indices)
    steps = 0
    while nums[0] != 0:
        search_idx = nums[0]
        value_to_move = nums[search_idx]
        nums.pop(search_idx)
        nums.insert(0, value_to_move)
        steps += 1
        
    return steps
