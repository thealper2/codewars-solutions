def special_number(number):
    i = 0
    while 10 ** i <= number:
        d = number // 10 ** i % 10
        if d > 5:
            return "NOT!!"
        
        i += 1
        
    return "Special!!"
