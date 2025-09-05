def reverse(lst):
    empty_list = list()
    n = len(lst)
    for i in range(n):
        empty_list.append(lst[n - i - 1])
        
    return empty_list
    
    
