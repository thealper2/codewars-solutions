def fibs_fizz_buzz(n):
    if n == 0:
        return []
    
    fib = [1, 1]
    if n == 1:
        return [1]
    
    if n == 2:
        return [1, 1]
    
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
        
    result = []
    for num in fib:
        if num % 15 == 0:
            result.append("FizzBuzz")
            
        elif num % 3 == 0:
            result.append("Fizz")
            
        elif num % 5 == 0:
            result.append("Buzz")
            
        else:
            result.append(num)
            
    return result
