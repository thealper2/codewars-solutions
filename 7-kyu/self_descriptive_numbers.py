def self_descriptive(num):
    num_str = str(num)
    n = len(num_str)
    for i in range(n):
        if num_str.count(str(i)) != int(num_str[i]):
            return False
        
    return True
