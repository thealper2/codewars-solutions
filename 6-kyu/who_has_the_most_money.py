def most_money(students):
    if len(students) == 1:
        return students[0].name
    
    max_money = float('-inf')
    max_student = None
    for s in students:
        money = s.fives * 5 + s.tens * 10 + s.twenties * 20
        s.money = money
        if money > max_money:
            max_student = s.name
            max_money = money
            
    if all(s.money == max_money for s in students):
        return "all"
    
    return max_student