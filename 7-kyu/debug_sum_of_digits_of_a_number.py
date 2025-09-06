def get_sum_of_digits(num):
    sum = 0
    s = str(num)
    digits = list(s)
    for x in digits:
        sum += int(x)
        
    return sum
