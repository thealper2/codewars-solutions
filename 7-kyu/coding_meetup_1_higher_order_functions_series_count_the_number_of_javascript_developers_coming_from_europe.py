def count_developers(lst):
    count = 0
    for user in lst:
        if user['continent'] == 'Europe' and user['language'] == 'JavaScript':
            count += 1
            
    return count