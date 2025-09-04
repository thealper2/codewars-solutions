def sum_factorial(lst):
    def factorial(n):
        if n < 2:
            return 1
        else:
            return n * factorial(n-1)
        
    return sum([factorial(num) for num in lst])
