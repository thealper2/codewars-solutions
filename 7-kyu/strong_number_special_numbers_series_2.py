def strong_num(number):
    factorials = [0] * 10
    factorials[0] = factorials[1] = 1
    for i in range(2, 10):
        factorials[i] = factorials[i - 1] * i

    fact_sum = 0
    temp = number

    while temp:
        fact_sum = fact_sum + factorials[temp % 10]
        temp = temp // 10

    return "STRONG!!!!" if fact_sum == number else "Not Strong !!"
