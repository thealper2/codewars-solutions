def is_it_a_num(s: str) -> str:
    nums = ''
    for c in s:
        if c.isdigit():
            nums += c
            
            
    if len(nums) == 11 and nums[0] == '0':
        return nums
    
    return 'Not a phone number'
    
