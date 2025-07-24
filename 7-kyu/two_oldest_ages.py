def two_oldest_ages(ages):
    oldest_age = float('-inf')
    second_oldest_age = float('-inf')
    
    for age in ages:
        if age > second_oldest_age:
            second_oldest_age = age
            if second_oldest_age > oldest_age:
                second_oldest_age, oldest_age = oldest_age, second_oldest_age
                
    return [second_oldest_age, oldest_age]