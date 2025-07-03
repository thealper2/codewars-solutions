def greet_developers(lst): 
    for user in lst:
        user['greeting'] = 'Hi ' + user['firstName'] + ', what do you like the most about ' + user['language'] + '?'
        
    return lst