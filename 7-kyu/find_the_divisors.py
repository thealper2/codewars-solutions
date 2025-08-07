def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)
        
    return result if result else f'{integer} is prime'
