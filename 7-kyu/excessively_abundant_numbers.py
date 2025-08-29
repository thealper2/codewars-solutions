def abundant_number(num):
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += i
            
    return divisors > num
